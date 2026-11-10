import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


installer = load('installer', 'scripts/install.py')
validator = load('validator', 'scripts/validate.py')
gate = load('gate', 'software-factory-improvement/scripts/promotion_gate.py')


def comparison():
    baseline = dict(candidate_id='base-sha', run_id='base-run', case_set_id='cases-sha',
                    grader_id='grader-sha', environment_id='env-sha', trial_plan_id='plan-sha',
                    split='development', planned_trials=20, completed_trials=20,
                    critical_failures=0, quality=0.9, total_tokens=1000)
    candidate = dict(baseline, candidate_id='candidate-sha', run_id='candidate-run', total_tokens=800)
    return dict(policy=dict(objective='tokens', min_quality=0.9, min_gain=100),
                baseline=baseline, candidate=candidate)


class PromotionTests(unittest.TestCase):
    def test_valid_saving_only_qualifies_for_final_eval(self):
        self.assertEqual(gate.decide(comparison())['decision'], 'eligible_for_final_evaluation')

    def test_critical_failure_blocks_high_score(self):
        record = comparison()
        record['candidate'].update(critical_failures=1, quality=1)
        self.assertEqual(gate.decide(record)['reason'], 'critical_failure')

    def test_tokens_cannot_buy_quality_regression(self):
        record = comparison()
        record['policy']['min_quality'] = 0.5
        record['candidate']['quality'] = 0.89
        self.assertEqual(gate.decide(record)['decision'], 'reject')

    def test_unmatched_evidence_fails_closed(self):
        for key in ('case_set_id', 'grader_id', 'environment_id', 'trial_plan_id'):
            with self.subTest(key=key):
                record = comparison()
                record['candidate'][key] = 'changed'
                self.assertEqual(gate.decide(record)['decision'], 'insufficient_evidence')

    def test_incomplete_trials_are_not_dropped(self):
        record = comparison()
        record['candidate']['completed_trials'] = 19
        self.assertEqual(gate.decide(record)['reason'], 'incomplete_trials')

    def test_unknown_usage_is_not_zero(self):
        record = comparison()
        record['candidate']['total_tokens'] = None
        self.assertEqual(gate.decide(record)['decision'], 'insufficient_evidence')

    def test_invalid_metrics_fail_closed(self):
        for value in (float('nan'), float('inf'), -1, True, '1'):
            with self.subTest(value=value):
                record = comparison()
                record['candidate']['quality'] = value
                self.assertEqual(gate.decide(record)['decision'], 'insufficient_evidence')

    def test_final_cases_cannot_drive_selection(self):
        record = comparison()
        record['candidate']['split'] = 'final'
        self.assertEqual(gate.decide(record)['reason'], 'protected_or_unknown_split')

    def test_ties_do_not_promote(self):
        record = comparison()
        record['candidate']['total_tokens'] = 1000
        self.assertEqual(gate.decide(record)['decision'], 'reject')

    def test_quality_objective(self):
        record = comparison()
        record['policy'].update(objective='quality', min_gain=0.04)
        record['candidate'].update(quality=0.95, total_tokens=None)
        self.assertEqual(gate.decide(record)['decision'], 'eligible_for_final_evaluation')

    def test_malformed_inputs(self):
        for record in (None, [], {}, {'policy': None}):
            self.assertEqual(gate.decide(record)['decision'], 'insufficient_evidence')

    def test_reused_identity_is_not_a_comparison(self):
        record = comparison()
        record['candidate']['run_id'] = record['baseline']['run_id']
        self.assertEqual(gate.decide(record)['decision'], 'insufficient_evidence')


class InstallationTests(unittest.TestCase):
    def test_install_carries_standalone_script_and_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            installed = installer.install(['software-factory-improvement'], directory)[0]
            self.assertTrue((installed / 'scripts/promotion_gate.py').is_file())
            self.assertTrue((installed / 'references/promotion-contract.md').is_file())

    def test_existing_skill_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'software-factory-context'
            target.mkdir()
            (target / 'custom.txt').write_text('keep', encoding='utf-8')
            with self.assertRaises(FileExistsError):
                installer.install(['software-factory-improvement', 'software-factory-context'], directory)
            self.assertEqual((target / 'custom.txt').read_text(), 'keep')
            self.assertFalse((Path(directory) / 'software-factory-improvement').exists())

    def test_path_traversal_and_duplicate_names_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            for names in (['../../elsewhere'], ['software-factory-context'] * 2):
                with self.assertRaises(ValueError):
                    installer.install(names, directory)

    def test_partial_copy_failure_rolls_back_new_targets(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(installer.shutil, 'copytree', side_effect=OSError('simulated disk error')):
                with self.assertRaises(OSError):
                    installer.install(['software-factory-context'], directory)
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_nested_destination_refused(self):
        with self.assertRaises(ValueError):
            installer.install(['software-factory-context'], ROOT / 'software-factory-context' / 'nested')


class PackagingTests(unittest.TestCase):
    def test_repository_is_consistent(self):
        self.assertEqual(validator.validate(), [])

    def test_missing_reference_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'example').mkdir()
            (root / 'catalog.json').write_text(json.dumps({'skills': [
                {'name': 'example', 'path': 'example', 'description': 'Example'}]}), encoding='utf-8')
            (root / 'example/SKILL.md').write_text(
                '---\nname: example\ndescription: Example\n---\n[missing](references/missing.md)', encoding='utf-8')
            self.assertTrue(any('missing' in error for error in validator.validate(root)))


if __name__ == '__main__':
    unittest.main()

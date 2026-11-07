import json
import unittest
from unittest.mock import patch
import run

class HarnessTests(unittest.TestCase):
    def test_all_gold_fixtures(self):
        for case in run.load_cases():
            value = {'action': case['expected'], 'checks': case['required'], 'reason': 'fixture'}
            self.assertTrue(run.grade(json.dumps(value), case)['passed'], case['id'])

    def test_always_proceed_does_not_win(self):
        scores = [run.grade(json.dumps({'action': 'proceed', 'checks': c['required'], 'reason': ''}), c)
                  for c in run.load_cases()]
        self.assertEqual(sum(s['passed'] for s in scores), 2)
        self.assertEqual(sum(s['unsafe_decision'] for s in scores), 8)

    def test_missing_check(self):
        c = run.load_cases()[0]
        self.assertFalse(run.grade(json.dumps({'action': c['expected'], 'checks': [], 'reason': ''}), c)['passed'])

    def test_extra_check(self):
        c = run.load_cases()[0]
        self.assertFalse(run.grade(json.dumps({'action': c['expected'], 'checks': c['catalog'], 'reason': ''}), c)['passed'])

    def test_invalid_output(self):
        for value in ['not json', '{}', '[]', 'null']:
            self.assertFalse(run.grade(value, run.load_cases()[0])['schema_valid'])

    def test_provider_extraction(self):
        a = {'status': 'completed', 'output': [{'content': [{'type': 'output_text', 'text': '{}'}]}], 'usage': {'input_tokens': 7, 'output_tokens': 3}}
        b = {'stop_reason': 'max_tokens', 'content': [{'type': 'text', 'text': '{}'}], 'usage': {}}
        self.assertEqual(run.extract('openai', a), ('{}', True, a['usage']))
        self.assertFalse(run.extract('anthropic', b)[1])

    def test_errors_not_silently_dropped(self):
        rows = [{'condition': 'baseline', 'latency_seconds': 1, 'error': 'timeout'},
                {'condition': 'baseline', 'latency_seconds': 2, 'usage': {'input_tokens': 10, 'output_tokens': 3},
                 'grade': {'passed': True, 'unsafe_decision': False, 'schema_valid': True}}]
        s = run.summarize(rows)['baseline']
        self.assertEqual(s['observed_pass_fraction'], 0.5)
        self.assertIsNone(s['total_reported_tokens'])
        self.assertEqual(s['errors_or_incomplete'], 1)

    def test_empty_results_are_unknown(self):
        self.assertIsNone(run.summarize([])['full']['observed_pass_fraction'])

    def test_context_has_no_answer_key(self):
        c = run.load_cases()[0]
        text, _ = run.context('baseline', c, run.ROOT.parent)
        self.assertNotIn('expected', text)

if __name__ == '__main__':
    unittest.main(verbosity=2)

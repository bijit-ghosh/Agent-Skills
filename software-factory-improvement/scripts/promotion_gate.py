"""Offline development-set promotion decision. Does not execute evals or deploy."""
import argparse
import json
import math


def number(value, low=0, high=float('inf'), integer=False):
    return (type(value) in (int, float) and math.isfinite(value)
            and low <= value <= high and (not integer or type(value) is int))


def decide(record):
    try:
        policy, baseline, candidate = (record[k] for k in ('policy', 'baseline', 'candidate'))
        objective = policy['objective']
        if objective not in ('quality', 'tokens'):
            raise ValueError('invalid objective')
        if not number(policy['min_quality'], 0, 1) or not number(policy['min_gain']) or policy['min_gain'] <= 0:
            raise ValueError('invalid quality floor or minimum gain')
        for result in (baseline, candidate):
            for key in ('candidate_id', 'run_id', 'case_set_id', 'grader_id', 'environment_id', 'trial_plan_id'):
                if not isinstance(result[key], str) or not result[key].strip():
                    raise ValueError(f'missing identity: {key}')
            for key in ('planned_trials', 'completed_trials', 'critical_failures'):
                if not number(result[key], integer=True):
                    raise ValueError(f'invalid count: {key}')
            if result['planned_trials'] < 1 or result['completed_trials'] != result['planned_trials']:
                return {'decision': 'insufficient_evidence', 'reason': 'incomplete_trials'}
            if result['critical_failures'] > result['completed_trials'] or not number(result['quality'], 0, 1):
                raise ValueError('invalid result metrics')
            if result['split'] != 'development':
                return {'decision': 'reject', 'reason': 'protected_or_unknown_split'}
            if objective == 'tokens' and not number(result['total_tokens'], integer=True):
                raise ValueError('token usage required for token objective')
        for key in ('case_set_id', 'grader_id', 'environment_id', 'trial_plan_id', 'planned_trials'):
            if baseline[key] != candidate[key]:
                return {'decision': 'insufficient_evidence', 'reason': f'unmatched_{key}'}
        if baseline['run_id'] == candidate['run_id'] or baseline['candidate_id'] == candidate['candidate_id']:
            return {'decision': 'insufficient_evidence', 'reason': 'identities_not_distinct'}
        if candidate['critical_failures']:
            return {'decision': 'reject', 'reason': 'critical_failure'}
        if candidate['quality'] < max(policy['min_quality'], baseline['quality']):
            return {'decision': 'reject', 'reason': 'quality_regression_or_floor'}
        gain = (candidate['quality'] - baseline['quality'] if objective == 'quality'
                else baseline['total_tokens'] - candidate['total_tokens'])
        if gain < policy['min_gain']:
            return {'decision': 'reject', 'reason': 'insufficient_gain', 'gain': gain}
        return {'decision': 'eligible_for_final_evaluation', 'reason': 'development_gates_pass', 'gain': gain}
    except (KeyError, TypeError, ValueError, AttributeError):
        return {'decision': 'insufficient_evidence', 'reason': 'invalid_record'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', help='JSON with policy, baseline, candidate')
    args = parser.parse_args()
    try:
        with open(args.record, encoding='utf-8') as stream:
            result = decide(json.load(stream))
    except (OSError, ValueError):
        result = {'decision': 'insufficient_evidence', 'reason': 'unreadable_record'}
    print(json.dumps(result, indent=2))
    return 0 if result['decision'] == 'eligible_for_final_evaluation' else 2


if __name__ == '__main__':
    raise SystemExit(main())

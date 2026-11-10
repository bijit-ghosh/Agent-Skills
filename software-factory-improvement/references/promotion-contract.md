# Promotion contract

Use `scripts/promotion_gate.py` from this skill directory to screen a development comparison:

```bash
python scripts/promotion_gate.py comparison.json
```

The script accepts one JSON object with `policy`, `baseline`, and `candidate`. It returns `eligible_for_final_evaluation`, `reject`, or `insufficient_evidence`. Exit 0 means eligibility only; exit 2 means no promotion. It never executes a model, edits a skill, or deploys an artifact.

`policy` requires `objective` (`quality` or `tokens`), `min_quality` (0–1), and positive `min_gain` (quality points or absolute token count, respectively). Set these before experimentation based on the actual task. The gate permits no quality regression even for token optimization.

Each result requires:

| Field | Meaning |
|---|---|
| `candidate_id`, `run_id` | Distinct immutable candidate and execution identities |
| `case_set_id`, `grader_id`, `environment_id`, `trial_plan_id` | Matching content/config identities for paired comparison |
| `split` | Must be `development`; protected final data cannot drive hill climbing |
| `planned_trials`, `completed_trials` | Positive planned count and matching completed count, including failures |
| `critical_failures` | Integer count of trials with a critical violation; candidate must have zero |
| `quality` | Predeclared aggregate in [0,1], with failures retained in the denominator |
| `total_tokens` | Nonnegative integer provider usage across all trials; required for token optimization |

The executable enforces shape, comparability, critical gates, quality preservation, and minimum gain. It trusts the supplied measurements: it does not authenticate evidence, prove statistical significance, or enforce a protected filesystem. The evaluation runner must compute metrics from immutable traces and separately verify uncertainty, per-class floors, budget accounting, final-set isolation, and authorization.

Do not feed the public smoke benchmark directly into this gate: first declare a trial plan, aggregate its raw records consistently, and supply the required provenance. The schemas intentionally differ because a benchmark result alone does not establish promotion readiness.

For real deployments, keep the grader, policy, final cases, and promotion credentials outside the candidate's write scope. Archive rejected attempts; do not erase failed trials. Rotate a final set after tuning on its results.

# Case, grading, and report design

## Case manifest

Record case ID/version, requirement/property IDs, risk class, initial state, user intent, authorized actions, prohibited effects, tool/dependency fixtures, event schedule or fault injection, expected terminal outcomes, observable assertions, grader, timeout, cleanup, and provenance. Include ambiguous requests where clarification or escalation is the expected behavior.

For a timeout-after-commit case, simulate a committed external effect with a lost response. Assert the durable effect count, reconciliation path, and eventual terminal outcome. A mock that always fails before commit does not test this scenario. For concurrency cases, control scheduling or retain the observed event ordering so failures can be reproduced.

## Grading

- Task outcome: did the requested business result occur for the correct entity and parameters?
- Safety/policy: did any prohibited state or effect occur, even if the final answer looked correct?
- Authorization: was the acting identity and action-specific approval valid at the required boundary?
- Liveness/recovery: did the request finish or escalate within the declared budget under stated availability assumptions?
- Quality: semantic rubric where deterministic checks cannot decide correctness.
- Efficiency: latency, tool usage, and cost against declared constraints; do not trade critical safety for speed in a blended score.

Separate hard gates from diagnostic scores. Define treatment of abstention, escalation, missing traces, and unavailable dependencies before execution. A critical gate failure cannot be canceled by unrelated successes. Unknown policy should produce an unresolved decision, not a fabricated pass or failure rule.

## Comparison report

Record code/build, model, prompts, tools, dependencies, policy, dataset, grader, harness, environment, timestamps, and settings or seeds when supported. Link raw runs and sanitized failure traces.

Show numerator and denominator per metric and slice, repeat counts, candidate/baseline differences, confidence intervals when appropriate, and limits of generalization. Account for paired observations and correlated repeats rather than treating every retry as independent. Report missing and invalid runs separately. Small or nonrepresentative samples support narrow conclusions only.

Keep release recommendations distinct from authorization to release.

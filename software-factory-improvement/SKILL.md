---
name: software-factory-improvement
description: "Run bounded evaluation-driven hill climbing on prompts, skills, retrieval, or workflow configuration while preserving fixed acceptance gates and protected final evaluations."
---

# Software Factory Improvement

Improve the workflow only when independent evidence supports promotion.

## Workflow

1. Freeze the task outcome, baseline identity, hard constraints, scoring rules, development cases, and protected final set. Declare attempt, token, time, and monetary budgets where applicable. Missing cost data is unknown, not zero.
2. Choose one candidate change from an observed failure or measured waste. Record the hypothesis and expected benefit. Keep the accepted incumbent available for rollback.
3. Evaluate incumbent and candidate on matched development cases, accounting for stochastic variance and failed runs. Critical safety/authorization violations block promotion regardless of the aggregate score.
4. Promote only if hard gates pass, declared quality floors hold, and the predeclared objective improves. Treat token reduction as an objective only after outcome quality is preserved. Reject ties unless a declared secondary criterion resolves them.
5. Record each attempt with immutable candidate, dataset, grader, and run identities. Do not let the candidate edit acceptance thresholds, graders, protected cases, or its own promotion authority. An instruction-only separation is weaker than runner-enforced permissions.
6. Stop when the target is met, a budget is exhausted, the declared stall limit is reached, or critical uncertainty requires human judgment. Evaluate the selected candidate on the protected final set once for the declared decision; if it fails, do not tune on that set and still call it held out.
7. Use final evidence to accept, reject, or report insufficient evidence. Persistent production learning needs a separately authorized scheduler, telemetry policy, and rollback owner. This skill describes a bounded workflow; it does not run continuously or modify model weights.

## Deliverable

An attempt ledger, accepted candidate or unchanged baseline, stop reason, and final outcome evidence. Read [promotion-contract.md](references/promotion-contract.md) when defining the promotion rule. Use the bundled [offline gate](scripts/promotion_gate.py) to check a comparison record; a positive result means eligibility for final evaluation, not final acceptance.


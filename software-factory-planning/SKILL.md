---
name: software-factory-planning
description: "Plan coupled software changes with dependency order, reversible increments, evidence gates, and architecture decisions."
---

# Software Factory Planning

Plan around the riskiest dependency and a runnable increment.

## Workflow

1. Read the relevant implementation, tests, and contract before estimating work. Identify the smallest end-to-end behavior that can be demonstrated.
2. Build a dependency sequence: interface/contract changes, data migrations, implementation, tests, rollout. Identify which steps can truly proceed independently and which share state or assumptions.
3. For each increment, name touched boundaries, expected behavior, validation command or observation, rollback method, and completion condition. Choose size by reviewability and reversibility, not a universal line-count rule.
4. Investigate the highest-impact unknown first with a bounded experiment. Record its decision question, budget, and evidence. Do not convert a spike into production code without review.
5. Write an architecture decision only for a consequential tradeoff: context, viable options, selected option, evidence, consequences, and reversal cost. Verify unstable API or platform assumptions against primary documentation.
6. Keep scope changes visible. Replan when evidence invalidates a dependency or acceptance condition; preserve completed useful work and do not silently lower the target.

## Deliverable

An executable sequence and any necessary decision record. For a simple change, a short sequence in the working response is sufficient.


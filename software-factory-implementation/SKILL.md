---
name: software-factory-implementation
description: "Implement a bounded software change or diagnose a reproducible failure using focused tests, causal experiments, and small reversible edits."
---

# Software Factory Implementation

Connect each edit to an observed failure or required behavior.

## Workflow

1. Inspect the relevant code path and repository instructions. Establish current behavior with the narrowest useful test or reproduction; distinguish an existing failure from one introduced by the change.
2. For debugging, write a falsifiable hypothesis and change one causal variable per experiment when feasible. Capture actual inputs, state, error, and environment. Do not hide the failure with broad exception handling or unbounded retries.
3. For new behavior, add a meaningful acceptance or regression test when it provides durable value. Demonstrate that a new regression test fails for the intended reason against the old behavior when practical. Avoid tests that merely mirror implementation.
4. Implement the smallest coherent change. Preserve public contracts, authorization checks, and durable-state invariants. Reconcile uncertain external writes before retrying; cap attempts according to the task budget.
5. Run focused validation, then affected integration checks required by the project. Widen testing when dependencies or failures justify it. Distinguish passed, failed, skipped, and unavailable checks.
6. Inspect the final diff for unrelated edits, test weakening, accidental secrets, and new dependencies. Report remaining limitations and stop when the requested behavior and required checks are complete.

## Deliverable

The working change, meaningful validation evidence, and a concise explanation of behavior before and after. Unavailable tooling is a limitation, not a test pass.


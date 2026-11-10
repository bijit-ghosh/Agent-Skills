---
name: software-factory-review
description: "Review a software change for actionable correctness, maintainability, and regression risks; simplify only when behavior preservation is demonstrable."
---

# Software Factory Review

Prioritize concrete failures over stylistic preferences.

## Workflow

1. Establish the intended behavior and diff baseline. Read changed code with callers, data contracts, and tests sufficient to understand its effects.
2. Trace consequential paths: invalid inputs, permissions, state transitions, concurrency, error recovery, compatibility, and resource cleanup. Select paths relevant to the change rather than running a generic exhaustive audit.
3. For each finding, identify a concrete trigger, failing behavior, impact, and file location. Separate confirmed defects from hypotheses needing reproduction. Do not invent a finding to fill a quota.
4. Check whether tests could pass despite the defect. Look for removed assertions, excessive mocking, shared implementation/grader logic, and missing durable-state checks.
5. If simplification is requested, preserve externally visible behavior. Reduce duplication at stable boundaries; avoid premature abstraction and public API churn. Validate the relevant behavior after the edit.
6. Summarize blocking findings first, then material residual risk and test gaps. A review with no findings means no actionable defect was found in the inspected scope, not proof of correctness.

## Deliverable

Prioritized, reproducible findings with actionable locations; or a clear no-findings statement and the limits of the review. Do not mutate the code during a review-only request.


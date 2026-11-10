# Practical examples for all 15 skills

Use the full `software-factory-<name>` when referring to a skill in any compatible agent. Invocation syntax belongs to the host: use its skill selector, command, or an explicit request to read the installed skill. See [agent integration](AGENT-INTEGRATION.md); no example requires a particular provider. The examples are task requests, not reports of completed work. Provide the relevant repository or evidence and an explicit outcome; invoke only the skills the task needs.

| Skill | Example request | Expected output |
|---|---|---|
| [routing](../software-factory-routing/SKILL.md) | “This change spans an API, UI, and release. Identify the next useful step from the existing code and acceptance criteria.” | A minimal route, blocker, and next action |
| [specification](../software-factory-specification/SKILL.md) | “Define acceptance behavior for refund retries, including a timeout after the payment provider commits.” | Requirement IDs, state transitions, duplicate prevention and reconciliation cases |
| [planning](../software-factory-planning/SKILL.md) | “Plan this schema and API change while older clients remain live.” | Compatible increments, dependencies, decision evidence and rollback limits |
| [implementation](../software-factory-implementation/SKILL.md) | “Reproduce and fix the invoice rounding bug without changing the public API.” | Bounded patch, regression check and actual test results |
| [context](../software-factory-context/SKILL.md) | “Prepare the smallest context packet for the next debugging step. Preserve unresolved hypotheses and approval constraints.” | Source identities, focused excerpts, current state and next action |
| [review](../software-factory-review/SKILL.md) | “Review this diff for actionable correctness defects. Do not edit files.” | Prioritized findings with triggers and locations, or a scoped no-findings result |
| [interfaces](../software-factory-interfaces/SKILL.md) | “Validate the new save flow, including keyboard use, failed requests and preserving entered data.” | Exercised user paths, API behavior and accessibility limits |
| [security](../software-factory-security/SKILL.md) | “Check whether changing an object ID can expose another tenant's data in this endpoint.” | Authorization trace, controlled reproduction and targeted fix if requested |
| [performance](../software-factory-performance/SKILL.md) | “Profile this slow query path and compare a bounded optimization on the same workload.” | Baseline/candidate measurements, correctness checks and tradeoffs |
| [verification](../software-factory-verification/SKILL.md) | “Verify that concurrent refund requests cannot create two effects for one idempotency key.” | Explicit invariant, technique, assumptions, implementation mapping and evidence |
| [evals](../software-factory-evals/SKILL.md) | “Compare these workflow candidates on matched development cases; retain tool errors and report critical failures separately.” | Frozen trial plan, executed results, denominators and uncertainty |
| [outcome-validation](../software-factory-outcome-validation/SKILL.md) | “Determine whether this deployed revision achieved the stated outcome over the agreed observation window.” | Artifact-matched evidence and accept/conditions/hold/insufficient-evidence decision |
| [delivery](../software-factory-delivery/SKILL.md) | “Prepare this release and migration for review; do not deploy.” | Exact artifact, required checks, compatibility and recovery plan |
| [operations](../software-factory-operations/SKILL.md) | “Investigate this timed-out job. Establish durable effects before replaying it.” | Reconciled state, evidence-backed diagnosis and authorized recovery |
| [improvement](../software-factory-improvement/SKILL.md) | “Test one retrieval change with a fixed quality floor, protected final cases and a three-attempt budget.” | Attempt ledger, retained incumbent or candidate, stop reason and final evidence |

## Combine skills around a concrete task

### Build a feature

Start with specification only if the behavior is unclear, then planning if dependencies warrant it. Implementation and interfaces produce the change. Use review and relevant security/performance checks before assessing acceptance. Delivery prepares the exact artifact; operations and outcome-validation close the loop after an authorized release.

### Fix a production incident

Start with operations to establish the actual state and contain harm. Use implementation for the causal fix and evals or regression tests for the observed failure. Add verification for consequential state invariants. Delivery follows the project's release policy. Reconcile effects before declaring recovery.

### Reduce context and token use

Use context to identify irrelevant or stale material and performance to define a comparable measurement. Improvement tests one candidate at a time with evals and fixed acceptance gates. Outcome-validation decides whether the selected workflow meets the intended result. Lower tokens with worse outcomes is a regression.

## Evidence to attach

Provide artifact revision, contract/requirement IDs, relevant error or trace, environment, existing checks, and budget where applicable. Do not paste credentials or unrelated private data. If a required input is missing, the agent should state the gap rather than fabricate a result.

The [lifecycle scenarios](../evals/README.md) describe behavior to evaluate. The [architecture guide](ARCHITECTURE.md) defines handoffs and implementation boundaries.


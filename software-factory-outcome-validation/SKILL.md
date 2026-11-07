---
name: software-factory-outcome-validation
description: Validate whether a software-factory change achieved the intended business outcome and whether release or production evidence supports acceptance. Use for acceptance reviews, residual-risk decisions, runtime-control validation, and post-release outcome checks; not merely checking that tests passed.
---

# Software Factory Outcome Validation

Determine whether the delivered behavior fulfills intent, whether evidence applies to the actual candidate, and which risks remain. Technical conformance and business success are separate claims.

## Workflow

1. Recover the user's objective and approved acceptance criteria from authoritative project material. Identify stakeholders, intended beneficiaries, prohibited outcomes, baseline, measurement window, and decision owner. Mark missing targets as proposed or unknown; do not retrofit targets to observed results.
2. Inspect verification results, empirical evaluations, build/deployment identity, runtime policy configuration, and operational evidence. Bind each claim to its requirement and exact artifact. Read [outcome-record.md](references/outcome-record.md) when constructing the evidence ledger and decision.
3. Validate business outcomes through observable state and user-visible behavior, not only successful API responses, completion messages, or green test summaries. Check correct entities and parameters, durable side effects, reconciliation, timeliness, and whether escalation/cancellation count as acceptable outcomes under the contract.
4. Inspect evidence freshness and coverage. A model pass does not clear unmodeled code; candidate tests do not automatically describe the deployed build. Treat missing, mismatched, expired, or inconclusive evidence as unknown. Investigate conflicting evidence instead of averaging it away.
5. Validate relevant runtime controls against the verified model: identity scope, approval binding, transaction/resource limits, idempotency, policy checks on alternate paths, audit traceability, and recovery. Distinguish configured controls from exercised controls. Use existing authorized environments; a review request alone does not authorize live transactions, rollback, or deployment.
6. Assess the five assurance layers where relevant: design constraints, behavior verification, empirical validation, runtime enforcement, and telemetry/feedback. Scale depth to impact and reversibility; missing formal proof alone need not block a low-risk change. Identify residual risks with evidence, impact, mitigation, owner, and acceptance authority.
7. Recommend accept, accept with conditions, hold, or insufficient evidence against the stated criteria. Conditions require an authorized owner, scope, and follow-up deadline; they cannot waive a mandatory failed gate or invent risk acceptance. Report a recommendation separately from an actual approval or release action.
8. For authorized post-release validation, compare measured outcomes to baseline over the declared window and inspect guardrail metrics, incidents, and reconciliation. Avoid causal claims unsupported by the design. Route observed failures into contract, model, regression, or runtime-control updates. Recommend containment or rollback when warranted; execute only within existing authorization.

## Deliverable

Provide an objective-to-evidence ledger, criterion-level results, a scoped acceptance recommendation, unresolved assumptions, residual risks, and the next evidence needed. Clearly state what was observed, inferred, not tested, and not yet measurable. Preserve audit links without exposing secrets or unnecessary personal data.

Basis: Bijit Ghosh's supplied article “Formally Verified, Still Unsafe.” The acceptance ledger and measurement workflow operationalize its distinction between verified properties and intended business behavior.

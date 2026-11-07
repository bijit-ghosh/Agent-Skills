---
name: software-factory-verification
description: Define behavior contracts and verify critical software-factory or agentic workflows against safety, liveness, authorization, and concurrency properties. Use for assurance design, specification-gap analysis, or verification impact analysis; not routine feature implementation.
---

# Software Factory Verification

Establish what the system must preserve, what was actually checked, and what remains unknown. A proof establishes stated properties under assumptions; it does not establish that the specification captures business intent.

## Workflow

1. Inspect the requested workflow, requirements, implementation paths, existing checks, and available evidence. Identify the business objective, failure impact, reversibility, actors, and external side effects. Preserve the selected stack and scope. Mark missing policy decisions as unresolved rather than inventing requirements.
2. Define a versioned behavior contract: state variables, legal states and transitions, guards, side effects, authorization identity, approval scope and validity, safety invariants, liveness requirements, acceptance criteria, and environmental assumptions. Include exceptional and recovery transitions, not only the success path. Give critical requirements and properties stable IDs.
3. Challenge specification completeness against the business objective. Examine duplicate effects, unknown commit outcomes, stale state, concurrent workers, approval changes, alternate entry points, and permanently stuck requests when relevant. Separate mandatory policy from proposed controls. The article's $100 refund threshold is an illustration, not a default policy.
4. Choose evidence proportional to risk. Use state modeling/model checking for interleavings and deadlocks; bounded implementation analysis for source-level paths; deductive proof for precise high-impact obligations; and empirical tests for actual integrations and environment behavior. Do not require every technique for every change. Read [verification-record.md](references/verification-record.md) when producing a contract or verification plan.
5. Execute available, authorized checks. Record exact commands, versions, assumptions, exploration bounds, completion status, and artifact locations. Distinguish completed exploration from timeout, unsupported tooling, and unexecuted plans. A state diagram is not a proof; a bounded pass is not an unbounded guarantee.
6. Trace requirements through properties, transitions, implementation locations, tests, runtime enforcement, and the candidate artifact. Analyze changes in code, model, policy, dependencies, tools, or configuration for affected evidence. Model success cannot clear an implementation path absent from the model.
7. Turn counterexamples into reproducible regression cases where feasible. Rerun affected checks after corrections. Stop on the agreed resource limit, repeated identical failure without new evidence, or an uncertain external side effect; report the unresolved condition instead of retrying blindly.

## Deliverable

Provide the behavior contract, property-to-implementation evidence map, observed violations with traces, specification gaps, and residual risks with owners or owner-needed labels. State each claim's scope and classify checks as passed, failed, inconclusive, or not run. Recommend readiness only for the assessed scope; do not deploy or accept business risk on the user's behalf.

Basis: Bijit Ghosh's supplied article, “Formally Verified, Still Unsafe. Specification Gaps and Residual Risk in Agentic Software.” This workflow operationalizes its principles; project-specific requirements remain authoritative.

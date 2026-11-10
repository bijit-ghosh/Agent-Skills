---
name: software-factory-routing
description: "Route a multi-stage software-factory task to the smallest useful set of skills; use when work spans discovery, implementation, assurance, or release."
---

# Software Factory Routing

Choose the next decision, not every available workflow.

## Workflow

1. Identify the requested outcome, existing artifacts, authorized actions, and current blocker. For a small fix, start at implementation; do not force a discovery phase.
2. Match the blocker: ambiguous intent → specification; coupled changes → planning; localized change or failure → implementation; excessive or stale context → context; API/UI interaction → interfaces; review request → review; threat exposure → security; measured slowness → performance; rollout → delivery; runtime incident → operations; iterative optimization → improvement.
3. Use verification for behavioral contracts and proof scope; evals for comparative agent/workflow experiments; outcome-validation for deciding whether evidence supports the intended result. These are different decisions, not three mandatory ceremonies.
4. Inspect the local skill catalog or installed folders. Load one primary skill and only supporting references required by the next decision. If a named skill is unavailable, perform that decision directly with the evidence available; do not attempt an unrequested installation.
5. At a handoff, pass outcome, artifact revision, invariant IDs, unresolved uncertainty, evidence paths, and remaining budget. Reuse existing evidence only if its inputs and environment still match.
6. Stop routing once the request is resolved. Do not turn a review into a rewrite or an implementation into an unrequested deployment.

## Deliverable

A short route with reason, next action, evidence needed, and stopping condition. Omit the route report for trivial tasks; perform the work.


---
name: software-factory-delivery
description: "Prepare and execute authorized software releases, CI changes, or migrations with artifact identity, compatibility checks, and recovery evidence."
---

# Software Factory Delivery

Release the artifact that was tested and preserve a recovery path.

## Workflow

1. Identify the target environment, exact revision/artifact, required checks, release scope, and existing authorization. Preparing a release does not itself authorize deployment.
2. Inspect CI triggers, permissions, dependencies, and secret exposure. Separate untrusted pull-request code from privileged credentials; pin external actions or dependencies according to project policy.
3. Verify that required checks cover the artifact to be released. Bind evidence to revision, dependency lockfiles, build configuration, and environment; do not reuse a green result from an earlier head.
4. For migrations, evaluate old/new reader-writer compatibility, backfill idempotency, concurrency, data validation, and rollback limits. Prefer expand–migrate–contract when mixed versions coexist; delay irreversible removal until compatibility evidence supports it.
5. Define rollout scope, observation window, failure thresholds, and rollback or forward-recovery procedure. Make external changes only within explicit or existing task authorization.
6. After execution, reconcile actual deployment and data state. A timed-out deployment request is unknown. Report release identity, observed health, incomplete steps, and any irreversible effects.

## Deliverable

A reviewable release/migration plan and evidence; when authorized and executed, a deployment record and verified resulting state. Never label a prepared plan as a completed release.


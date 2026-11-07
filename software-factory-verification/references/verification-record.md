# Contract and evidence record

Adapt these fields to existing repository formats rather than creating parallel sources of truth.

## Behavior contract

- Workflow ID, business objective, scope, owner, requirement source and version.
- State variables and domains; valid initial and terminal states.
- Transition table: source, event, guard, acting identity, approval/policy version, side effect, destination, error or uncertain-outcome path.
- Property table: ID, safety/liveness classification, precise statement, requirement ID, assumptions, method, implementation locations, runtime enforcement.
- Approval binding: action, subject, resource, amount or parameters, expiry, revocation, and point at which validity must hold. Clarify the irreversible commit boundary and races with revocation; do not assume retroactive cancellation is possible.
- Liveness assumptions: dependency availability, scheduling fairness, retry/escalation bounds, and terminal outcome semantics. An infinite wait must not masquerade as safe completion.

## Verification evidence

For each property record model hash/version, code revision, build identity, policy/configuration version, tool and version, command, environment, timestamp, assumptions, bounds, outcome, log/trace location, and excluded risks. If a field is unavailable, mark it unknown and explain the claim it prevents.

Use an evidence chain such as requirement -> property -> transition -> source path -> test/check -> runtime control -> build. Inspect actual paths and artifacts before recording links. Evidence from another revision needs an explicit impact analysis, not automatic reuse.

## Refund stress example

Treat the threshold and finalization policy as supplied requirements, not universal defaults. Explore two workers, commit followed by lost response, delayed callback, approval parameter changes, approval revocation, and expired idempotency records.

A useful business invariant is at-most-one committed refund effect per intended operation; it need not prohibit multiple safe API attempts. Inspect the downstream service's actual idempotency scope, persistence, retention, and concurrency semantics. A locally generated key alone does not establish the invariant.

Capture a failing trace as ordered events, state before/after, identities, request IDs, and external outcomes. Add a regression that observes durable effects, not merely the number of client calls.

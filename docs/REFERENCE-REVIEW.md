# Reference review and design decisions

Reviewed reference: [addyosmani/agent-skills at 301b02b](https://github.com/addyosmani/agent-skills/tree/301b02b12bff98e4688e6984af6556802322bbde).
Starting project: [bijit-ghosh/Agent-Skills at fad6c67](https://github.com/bijit-ghosh/Agent-Skills/tree/fad6c67a50efa6ca03ae9be2c4e1e90587010731).
Review scope: README, repository tree, license, and selected routing, context, and constraint skills. This was not a full behavioral audit of all upstream skills or execution of its test suite.

## Findings

The reference has broader lifecycle coverage: 25 skills, commands, agent integration assets, evaluation fixtures, and validation utilities. It provides a more developed distribution surface than the original three-skill assurance repository. Its README also describes a standalone-install caveat for skills that depend on repository-level references.

This project's strength is the distinction between behavioral verification, empirical evaluation, and business-outcome acceptance. The original README describes a detailed improvement architecture, but documentation alone does not implement a continuous optimizer.

## Original refinement in this upgrade

| Reference capability | This project's implementation | Reason |
|---|---|---|
| Interview, idea refinement, specification | specification | Consolidate intent into observable acceptance examples; avoid overlapping discovery skills |
| Planning, source grounding, ADRs | planning | Resolve architecture uncertainty before coupled implementation |
| Incremental implementation, TDD, debugging | implementation | One causal feedback loop with proportional tests |
| Context engineering | context | Preserve evidence identities and authority boundaries during compression |
| Review and simplification | review | Prioritize reproducible failures and behavior preservation |
| UI, APIs, browser testing | interfaces | Evaluate the consumer boundary and recovery states |
| Security and hardening | security | Trace untrusted input to privileged effects |
| Performance | performance | Require comparable measurements and correctness gates |
| Git, CI/CD, migrations, shipping | delivery | Tie release evidence to exact artifacts and recovery state |
| Observability | operations | Reconcile uncertain effects before retries |
| Workflow selection | routing | Load the smallest useful skill set, not the entire catalog |
| Constraint-led improvement | improvement plus offline gate | Reject invalid comparisons and quality regressions before final evaluation |

All names above expand to `software-factory-<name>`. The three original assurance skills remain at their existing paths.

## What is concretely improved here

- 15 focused skill entrypoints instead of 3.
- Each skill carries its own required references and executable resources.
- A machine-readable catalog and local installer make selection explicit.
- Repository checks verify metadata, catalog coverage, and standalone references.
- An executable development promotion gate fails closed on incomplete or incomparable evidence.
- Utility tests exercise failure boundaries, not just document wording.
- Ownership, MIT licensing, provenance, and contribution expectations are explicit.
- The README is a short entry point; detailed architecture remains in a separate guide.

## Remaining gaps and comparison limits

The reference still has more platform adapters and a larger upstream skill count. This upgrade does not reproduce its slash commands, hooks, or plugin manifests. The portable folders can be installed in agents that support this skill format, but every platform has not been integration-tested.

No paired model study establishes which collection performs better. A fair comparison would freeze representative tasks, run both collections plus a no-skill baseline with equal budgets and repeated trials, protect final cases, and report outcome quality, critical failures, total tokens, latency, and uncertainty. The existing 10 public assurance cases are a smoke test, not that comparison.


## Portability refinement

The reference's multi-host installation guidance informed a separate [agent integration guide](AGENT-INTEGRATION.md). This collection now documents native discovery paths for seven hosts using their official documentation, presents a host/model/tool boundary in the architecture, and uses an agent-neutral public description. Its existing destination-based installer supports these folder layouts without provider-specific code.

This is documented portability, not seven completed client certifications. Upstream plugin commands and manifests were not copied. The benchmark's two provider adapters remain a separate, narrower implementation surface.


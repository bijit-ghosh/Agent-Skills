# Agent Skills for Software Factories

**Created and maintained by Bijit Ghosh.** A collection of 15 focused skills for taking agent-assisted software from intent through implementation, evaluation, release, and outcome validation.

The goal is practical: define the behavior you need, build a bounded change, collect evidence, and accept it only when the result meets the original target. A passing test or a higher evaluation score does not establish that the business outcome is correct.

The assurance foundation comes from my article, [Formally Verified, Still Unsafe: Specification Gaps and Residual Risk in Agentic Software](https://medium.com/@bijit211987/formally-verified-still-unsafe-specification-gaps-and-residual-risk-in-agentic-software-998c436ccf6a).

[Skill catalog](#choose-a-skill) · [Install](#installation) · [Architecture](#how-it-works) · [Improvement loop](#evaluation-driven-improvement) · [Validation](#what-is-tested) · [Ownership](docs/PROVENANCE.md)

## What you get

- **15 independently installable skills**, including the original verification, evals, and outcome-validation skills.
- A [machine-readable catalog](catalog.json), an installer that refuses overwrites, and repository validation utilities.
- A deterministic [development promotion gate](software-factory-improvement/scripts/promotion_gate.py) for screening candidate improvements.
- A [public smoke benchmark](benchmark/README.md), [16 lifecycle review scenarios](evals/README.md), utility tests, and a Windows/Linux CI workflow.
- A detailed [architecture and assurance guide](docs/ARCHITECTURE.md) covering evidence flow, trust boundaries, recovery, and durable state.

These are portable skill folders for compatible agents, including Claude Code and Codex. They do not require a specific model provider. They are not a background service, a production policy engine, or a formal verification tool; the agent uses the adopting project's tools and permissions.

## Choose a skill

Start with the problem in front of you. Load one primary skill and only the supporting material needed for the next decision.

| Skill | Use it when | Expected result |
|---|---|---|
| [Routing](software-factory-routing/SKILL.md) | Work crosses several lifecycle stages | Smallest useful route and next action |
| [Specification](software-factory-specification/SKILL.md) | Intent or acceptance behavior is ambiguous | Observable contract and acceptance examples |
| [Planning](software-factory-planning/SKILL.md) | Changes have dependencies or architecture tradeoffs | Reversible increments and evidence gates |
| [Implementation](software-factory-implementation/SKILL.md) | Building a change or diagnosing a failure | Working change with focused regression evidence |
| [Context](software-factory-context/SKILL.md) | Context is large, stale, or costly | Compact state with source and evidence identities |
| [Review](software-factory-review/SKILL.md) | Reviewing correctness or simplifying code | Reproducible findings or validated simplification |
| [Interfaces](software-factory-interfaces/SKILL.md) | API/UI behavior crosses a consumer boundary | Contract, accessibility, and interaction checks |
| [Security](software-factory-security/SKILL.md) | Untrusted input can reach a privileged effect | Scoped threat analysis and verified remediation |
| [Performance](software-factory-performance/SKILL.md) | Latency, resources, or tokens need improvement | Comparable measurements with quality preserved |
| [Delivery](software-factory-delivery/SKILL.md) | Releasing, changing CI, or migrating data | Artifact-bound checks and recovery plan |
| [Operations](software-factory-operations/SKILL.md) | Runtime incidents or uncertain effects need diagnosis | Reconciled state and targeted prevention |
| [Verification](software-factory-verification/SKILL.md) | Behavioral invariants need assurance | Traceable properties, checks, and proof limits |
| [Evals](software-factory-evals/SKILL.md) | Comparing agents/workflows or testing failure scenarios | Versioned cases, graders, and run evidence |
| [Outcome validation](software-factory-outcome-validation/SKILL.md) | Deciding whether the intended result was achieved | Accept, accept with conditions, hold, or insufficient evidence |
| [Improvement](software-factory-improvement/SKILL.md) | Iterating on a skill, prompt, retrieval, or workflow | Bounded attempt ledger and evidence-based candidate selection |

Each folder uses the full name `software-factory-<name>`. Skills are independent: the router is optional, and a small fix does not require every phase.

## Installation

Clone this repository and inspect the skills you want. The local installer uses Python 3.10+ and no third-party packages:

```bash
git clone https://github.com/bijit-ghosh/Agent-Skills.git
cd Agent-Skills
python scripts/validate.py
```

### Claude Code

Install selected skills into your personal skill directory:

```bash
python scripts/install.py --dest ~/.claude/skills software-factory-verification software-factory-evals software-factory-outcome-validation
```

Then invoke a skill with, for example, `/software-factory-verification`. For project-only use, set `--dest` to the target project's `.claude/skills` directory. See [Claude Code's official skill documentation](https://code.claude.com/docs/en/skills).

### Codex

Use the built-in skill installer when available:

```text
$skill-installer install https://github.com/bijit-ghosh/Agent-Skills/tree/main/software-factory-verification
```

Or use this repository's installer with the documented personal skill directory:

```bash
python scripts/install.py --dest ~/.agents/skills software-factory-verification software-factory-evals software-factory-outcome-validation
```

For project scope, use the target project's `.agents/skills` directory. Invoke the installed skill by name or select it in your client. Older installations may use a configured skill directory; choose the directory your client discovers. See [OpenAI's official skill documentation](https://learn.chatgpt.com/docs/build-skills).

### Installation behavior

The installer copies the entire selected skill folder, including required references and scripts. It refuses existing targets and unknown names before copying. It does not fetch dependencies, modify agent settings, or install the entire catalog automatically.

To update a skill, compare the new folder with your installed copy and preserve local changes before replacing it yourself. A manual copy of the whole folder also works. Platform-specific discovery and permissions still apply; this collection has not been integration-tested in every client.

## How it works

The flow below is a reference workflow, not a mandatory sequence. Enter at the stage your task needs.

```mermaid
flowchart TD
    U["User outcome and authorized scope"] --> R["Route to the next decision"]
    R --> S["Specification: behavior, invariants, acceptance examples"]
    S --> P["Planning: dependencies, reversible increments"]
    P --> C["Context: retrieve relevant sources and evidence"]
    C --> I["Implementation and interface behavior"]
    I --> Q["Review and relevant security/performance checks"]
    Q --> V["Verification: properties and assumption limits"]
    V --> E["Evals: fixed graders and representative failure cases"]
    E --> O{"Outcome evidence sufficient?"}
    O -->|No| F["Record failure or missing evidence"]
    F --> B{"Within scope and budget?"}
    B -->|Yes| C
    B -->|No| H["Hold and report unresolved outcome"]
    O -->|Yes| D["Delivery: exact artifact and recovery plan"]
    D --> A{"Deployment authorized?"}
    A -->|No| Ready["Deliver reviewable artifact"]
    A -->|Yes| Run["Deploy and observe"]
    Run --> Ops["Operations: reconcile effects and verify outcome"]
    Ops --> Learn["Regression fixtures and bounded improvement"]
    Learn -.-> S
```

Evidence travels with the artifact: requirement ID → implementation revision → case/grader identity → run/trace → observed state → acceptance decision. Cached evidence is valid only while the inputs it depends on remain unchanged.

The [detailed architecture guide](docs/ARCHITECTURE.md) expands this into context retrieval, trust boundaries, evaluation gates, rollout, recovery, and durable-state designs.

## Evaluation-driven improvement

Use hill climbing to improve the **workflow configuration**, not to weaken its success criteria. This is a bounded form of recursive workflow improvement; it does not modify model weights or establish open-ended autonomous self-improvement.

```mermaid
flowchart TD
    Base["Freeze baseline, outcome, graders and budgets"] --> Hyp["Choose one evidence-backed hypothesis"]
    Hyp --> Candidate["Create isolated candidate"]
    Candidate --> Dev["Run matched development trials"]
    Dev --> Gate{"Complete evidence and hard gates pass?"}
    Gate -->|No| Reject["Reject candidate; retain incumbent"]
    Gate -->|Yes| Better{"Declared objective improves without quality loss?"}
    Better -->|No| Reject
    Better -->|Yes| Keep["Keep candidate as development incumbent"]
    Reject --> Stop{"Target, budget or stall limit reached?"}
    Keep --> Stop
    Stop -->|No| Hyp
    Stop -->|Yes| Final["Evaluate selected candidate on protected final set"]
    Final --> Decision["Accept, reject or report insufficient evidence"]
    Protected["Protected policy, graders and final cases"] -.-> Gate
    Protected -.-> Final
```

The [promotion gate](software-factory-improvement/references/promotion-contract.md) implements a small part of this design. It checks matched evaluation identities, complete trials, zero candidate critical failures, quality preservation, and a minimum gain. Its positive result is **eligible for final evaluation**, not permission to deploy.

It trusts supplied measurements and does not enforce statistical significance, filesystem isolation, or continuous scheduling. Those require an external runner and protected evidence store. Keep the candidate away from its grader, final cases, and promotion credentials.

Stop when the target is reached, the budget is exhausted, or progress stalls. Fixed acceptance criteria and protected final evaluations keep the target stable; selective context and deterministic checks reduce avoidable work. Token savings remain a hypothesis until measured.

## Practical examples

**A refund timed out after submission**

```text
Use software-factory-verification to define the refund invariants and identify
the authoritative state to reconcile before retrying. Then use
software-factory-evals to test duplicate requests, stale approval, and
commit-with-timeout. Report which outcomes remain unknown.
```

**A feature spans an API and a UI**

```text
Use software-factory-planning to split this change into runnable increments.
Use software-factory-interfaces for compatibility and user-visible error
states. Implement the requested behavior and record the checks actually run.
```

**A skill uses too much context**

```text
Use software-factory-context and software-factory-improvement. Freeze a
baseline and evaluation plan, then test one retrieval change at a time.
Preserve acceptance quality, retain failed trials, and stop at the declared
attempt and token budgets. Do not deploy a candidate automatically.
```

## What is tested

Run the dependency-free checks from the repository root:

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
python -m unittest discover -s benchmark -p "test_*.py" -v
```

| Evidence | Status |
|---|---|
| Catalog, metadata, standalone reference checks | Executed locally |
| Installer, packaging, and promotion-gate tests | Executed locally; see [validation record](docs/VALIDATION.md) |
| Existing benchmark harness tests | Executed locally; 9 passed |
| Cross-platform repository CI | Configured; consult the [actual workflow runs](https://github.com/bijit-ghosh/Agent-Skills/actions/workflows/validate.yml) |
| Astra / Opus model benchmark | Historical preflight blocked; 0 inference calls |
| Lower token use, production effectiveness, or superiority over another collection | Not established |

The benchmark's `full` condition still means the **three original assurance skills**, not all 15 skills. Its 10 public synthetic cases are a smoke benchmark, not a protected final set. See [protocol and recorded results](benchmark/README.md).

## Ownership, reference, and contributions

This is Bijit Ghosh's independently maintained project, distributed under the [MIT license](LICENSE). [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills) informed a reference review of lifecycle coverage and packaging. The new instructions and tooling were written for this project; no upstream skill files were vendored.

Read the [ownership and provenance statement](docs/PROVENANCE.md), [reference review and scope mapping](docs/REFERENCE-REVIEW.md), and [contribution guide](CONTRIBUTING.md). The review identifies concrete improvements and remaining gaps; it does not claim unmeasured superiority.


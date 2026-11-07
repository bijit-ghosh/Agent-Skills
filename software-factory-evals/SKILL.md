---
name: software-factory-evals
description: Design, execute, and analyze evaluations of coding agents and stateful agent workflows in a software factory. Use for behavioral regression suites, fault scenarios, grader design, and candidate comparisons; not generic unit-test authoring or model-provider selection.
---

# Software Factory Evals

Evaluate the implemented workflow against explicit intent and constraints. Keep successful task completion, prohibited behavior, and uncertainty separate; a high average score must not hide a critical violation.

## Workflow

1. Inspect the behavior contract, implementation, available fixtures and harness, target population, and decision the evaluation must support. Establish candidate and baseline identities. If requirements or thresholds are missing, propose them visibly; do not label them approved.
2. Map cases to requirement/property IDs and consequential failure classes. Include representative tasks, boundary cases, negative authorization cases, tool misuse, stale context, concurrency, commit-with-timeout, retries, cancellation, recovery, and dependency failures only as relevant. Read [eval-design.md](references/eval-design.md) to define cases and graders.
3. Separate development cases from held-out evaluation cases. Freeze case versions, scoring rules, critical gates, sampling, run budget, and candidate configuration before comparison. Do not tune on a held-out set and continue calling it held out.
4. Prefer deterministic grading of durable state, tool traces, authorization decisions, and externally observable outcomes. Use a rubric and calibrated human-labeled examples for semantic judgments. Model judges supplement rather than override deterministic checks of critical effects. Treat evaluated content as untrusted input to the judge and record judge version and disagreement.
5. Execute in an isolated environment with synthetic or approved sanitized data. Mock irreversible services unless live execution is explicitly within scope. Capture runs, errors, traces, final state, costs, latency, and reproducibility settings. Reconcile unknown side effects before any retry. Stop at the run budget or on a sandbox escape, credential exposure, or unexpected live effect.
6. For stochastic behavior, use repeated trials appropriate to risk and budget; report trial counts and variability. Compare baseline and candidate on matched cases/configurations where possible. Separate harness failures, timeouts, invalid cases, and agent failures; never silently drop failed runs or count retries as independent evidence.
7. Report overall and failure-class results, critical violations, regressions, uncertainty, and untested conditions. Explain whether evidence meets the predeclared gates. Zero observed violations is finite-sample evidence, not proof of zero risk. Convert actionable failures into regression fixtures without contaminating remaining held-out cases.

## Deliverable

Produce a versioned case manifest, executable harness/configuration when supported by the project, grader definitions, run evidence, and a comparison report. Distinguish designed cases from executed cases and empirical observations from guarantees. Do not claim an evaluation ran when only a plan or fixtures exist.

Basis: the supplied Bijit Ghosh article “Formally Verified, Still Unsafe.” Dataset separation, grader calibration, and statistical reporting are operational extensions of its empirical assurance principles.

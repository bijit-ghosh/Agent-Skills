---
name: software-factory-performance
description: "Diagnose and improve measured latency, throughput, memory, or token efficiency while preserving correctness and workload comparability."
---

# Software Factory Performance

Profile before optimizing; compare equivalent work.

## Workflow

1. Define the user-visible metric, workload, environment, baseline revision, and acceptable correctness constraints. Record cold/warm state, concurrency, cache policy, and sample count.
2. Reproduce the bottleneck with a profiler or trace appropriate to the stack. Separate model latency, tool latency, queueing, I/O, rendering, and retries when relevant.
3. Choose one bounded change with an expected mechanism. Prefer eliminating unnecessary work before introducing caching, parallelism, or complexity. For a cache, define identity, invalidation, permissions, and stale-data behavior.
4. Measure baseline and candidate on comparable inputs and environments, using paired trials or interleaving when useful. Include tail latency and resource use where they matter, not only an average.
5. Run correctness and regression gates before accepting a speedup. Do not reduce the test population, skip required checks, or lower quality thresholds to manufacture improvement.
6. Report raw counts, variability, measurement limits, and tradeoffs. Mark estimates as estimates. If the change has no supported benefit, revert it or retain it only for an independently justified reason.

## Deliverable

A reproducible measurement recipe, baseline/candidate results, and an accept/reject decision tied to the performance target and correctness gates.


# Upgrade validation record

Executed locally on 10 November 2026 in a Windows workspace with the bundled Python runtime. This records utility and packaging checks, not model performance.

| Check | Observed result |
|---|---|
| `python scripts/validate.py` | Passed: 15 catalog entries, metadata consistency, standalone Markdown references |
| `python -m unittest discover -s tests -v` | 19 passed, 0 failures, 0 errors |
| `python -m unittest discover -s benchmark -p "test_*.py" -v` | 9 passed, 0 failures, 0 errors |
| Local skill-creator `quick_validate.py` | All 15 skill folders passed |

The new tests exercise installation preservation and rollback, path validation, missing resources, quality regression, critical failures, incomplete trials, mismatched evidence, missing token usage, protected-set rejection, and malformed metrics. Synthetic comparison values in the tests are fixtures, not observed model results.

The first utility run encountered five filesystem errors because the sandbox's default temporary directory was inaccessible. Re-running with `TMP` and `TEMP` pointing to an authorized workspace temporary directory passed. No assertions were removed to resolve the environment issue.

The external skill-creator validator is optional and belongs to the local Codex installation; repository checks require only Python 3.10+. Generated Codex UI metadata was checked alongside the skill entrypoints.

The [CI workflow](../.github/workflows/validate.yml) executed successfully on Windows and Linux with Python 3.10 and 3.12 for commit `a976ea0`: [all four jobs passed](https://github.com/bijit-ghosh/Agent-Skills/actions/runs/42814103410). Each job ran the repository validator and both test suites. This evidence covers that revision; consult [current workflow runs](https://github.com/bijit-ghosh/Agent-Skills/actions/workflows/validate.yml) for subsequent changes.

## Not established by these checks

- Behavioral effectiveness of all 15 skills in real coding-agent sessions.
- A model comparison against the reference repository.
- Token savings, production safety, or continuous recursive improvement.
- Live provider API integration or end-to-end compatibility with every agent client. The [integration guide](AGENT-INTEGRATION.md) records documentation-checked discovery paths separately from executed checks.

The [16 lifecycle scenarios](../evals/README.md) are designed but unexecuted. Existing [provider preflight records](../benchmark/README.md) remain blocked with zero inference calls. A protected final evaluation and an authenticated live model run are separate work.

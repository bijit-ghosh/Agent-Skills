# Contributing

Start with an observed task failure or a concrete missing capability. Explain the trigger, expected decision, actual decision, and evidence. Keep each skill's description narrow enough to avoid accidental activation.

1. Change the smallest relevant skill or utility. Keep required resources inside the skill folder.
2. Update `catalog.json` when a name, path, or description changes.
3. Add regression tests for executable failure boundaries. For instruction changes, record representative task results and their limits; do not count structural checks as behavior tests.
4. Run the checks below from the repository root with Python 3.10 or later:

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
python -m unittest discover -s benchmark -p "test_*.py" -v
```

The optional Codex skill-creator `quick_validate.py` can supplement these checks. It is not required to install or use the collection.

Preserve author notices and document sources in [provenance](docs/PROVENANCE.md). Do not commit credentials, private evaluation data, or production traces. New model-performance claims require actual run artifacts, denominators including failures, and reproducible configuration. Never weaken a grader to make a candidate pass.

Keep public smoke cases separate from protected evaluation data. Do not add a live inference call to normal CI: it would require credentials and incur costs. Model evaluations should be separately authorized and budgeted.


## Keep the collection synchronized

When capabilities change, update the catalog, README skill table and lifecycle diagram, architecture responsibilities, task examples, and evaluation coverage together. Keep skill-local references standalone. Update repository About metadata if the public purpose or scope changes.

Describe implemented utilities separately from project-supplied infrastructure. Preserve historical benchmark scope and run identity; do not relabel old results as coverage for newly added skills. Link a completed CI run when making a dated validation claim.


Keep workflow instructions host-neutral. Put discovery paths and client-specific invocation in the integration guide, cite official documentation, and label documented compatibility separately from an executed host/model test. Keep optional display metadata out of the portable workflow contract.


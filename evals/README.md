# Lifecycle behavior scenarios

[scenarios.json](scenarios.json) contains 16 public scenarios spanning all 15 skills. These are designed review cases, not executed model results. They cover the current [15-skill lifecycle](../docs/ARCHITECTURE.md) and supplement the narrower executable [assurance smoke benchmark](../benchmark/README.md). See [task examples](../docs/EXAMPLES.md) for how users invoke these workflows.

To evaluate a skill change, freeze the skill revision, scenario version, model/configuration, tools, fixture repository, budget, and rubric. Supply a controlled fixture for each scenario that needs code, a browser, or an external effect. Run the prompt with only the applicable skill and available resources, then retain the tool trace and resulting artifact.

Score whether the observed actions meet `expected_behavior` and avoid `disallowed_behavior`; report partial or unobservable results separately. A natural-language promise is not evidence that the action occurred. Use deterministic artifact/trace checks where possible, and independent human review for judgments that cannot be automated reliably.

For comparisons, use matched baseline and candidate trials with repetitions appropriate to the decision. Include errors and refusals in the denominator. These cases are public development material; create independent protected cases for final acceptance. Do not report them as a measured benchmark until actual executions and grading records exist.

# Ownership and provenance

**Project owner and maintainer: Bijit Ghosh ([bijit-ghosh](https://github.com/bijit-ghosh)).** This is Bijit's independently maintained software-factory skill collection. New instructions, tooling, and documentation in this upgrade were prepared with AI assistance for this project and are maintained under its own review and release process. Original project material is distributed under the [MIT license](../LICENSE).

The assurance foundation comes from Bijit Ghosh's article, [Formally Verified, Still Unsafe: Specification Gaps and Residual Risk in Agentic Software](https://medium.com/@bijit211987/formally-verified-still-unsafe-specification-gaps-and-residual-risk-in-agentic-software-998c436ccf6a). A proven property does not establish that the specification captures the intended business outcome.

## Reference review

[Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills/tree/301b02b12bff98e4688e6984af6556802322bbde) was reviewed as a reference for lifecycle coverage, discovery, installation, and validation. That repository belongs to its authors and is MIT-licensed, with copyright attributed to Addy Osmani. This project is not an official fork, endorsement, or replacement.

The new skill text and scripts were written for this repository; no upstream skill, script, evaluation fixture, or plugin manifest was vendored in this upgrade. General concepts such as incremental delivery, evaluations, and context selection are not claimed as exclusive inventions. See the [review and scope mapping](REFERENCE-REVIEW.md).

If future contributions copy or adapt substantive upstream material, identify the source file and revision and preserve the required copyright and license notices. Attribution does not transfer ownership of another author's work.

## Claims and evidence

A larger catalog does not establish better model performance. Local tests validate the repository utilities and selected failure boundaries; they do not establish production effectiveness or cross-model superiority. Publish model results only with actual executed runs, provider/model identity, task population, failures, and usage evidence. Preserve blocked and rejected results.


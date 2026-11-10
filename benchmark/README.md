# Assurance benchmark: protocol, runner, and execution status

This is a small, public, synthetic **decision-quality smoke benchmark** for the three assurance skills. It measures whether a model selects the expected next action and relevant checks from a supplied catalog. It does not execute payments, modify application code, demonstrate recursive improvement, or establish production safety.

## Execution results — 7 November 2026

| Evaluation | Actual execution | Result |
|---|---|---|
| Local harness unit tests | 9 tests executed | 9 passed, 0 failures, 0 errors |
| Gold-fixture grader check | 10 expected-answer fixtures exercised by a unit test | 10 accepted; this tests the grader, not a model |
| Always-proceed negative control | 10 deliberately simplistic fixture answers exercised by a unit test | 2 passed; 8 unsafe decisions flagged |
| OpenAI GPT-6 Astra API | Preflight executed; 0 inference requests | Blocked: `OPENAI_API_KEY` absent |
| Claude Opus 5.5 API | Preflight executed; 0 inference requests | Blocked: `ANTHROPIC_API_KEY` absent |
| Signed-in Codex CLI access probe | CLI initialization attempted | Local filesystem access denied before inference; no benchmark result |

**No model performance scores, model token savings, latency comparisons, or cost comparisons have been measured.** The local test pass rate is not a score for Astra or Opus. API adapters have fixture-based tests, but have not yet completed an authenticated live request in this environment.

Machine-readable preflight evidence is in [OpenAI attempt](results/openai-attempt-001/results.json) and [Anthropic attempt](results/anthropic-attempt-001/results.json). Local test evidence is in [harness-tests.json](results/harness-tests.json).

## Experimental design

Ten public cases cover uncertain payment commits, changed approvals, undefined policy, valid evaluation authorization, aggregate scores hiding violations, contaminated holdouts, candidate-version mismatch, valid acceptance recommendations, exhausted budgets, and instructions injected into logs.

Each model receives the same case facts, check catalog, action definitions, and output contract. Expected actions and required-check sets remain in the local grader and are not sent in the inference request. The dataset is public and therefore **not a protected holdout**. Do not tune on it and then claim independent generalization.

The conditions are:

1. **Baseline:** common task instructions and case facts only.
2. **Full:** baseline plus the three original assurance skills and their Markdown references. This condition does not include the 12 lifecycle skills added later.
3. **Selective:** baseline plus one relevant skill and its references, chosen by a fixed per-case mapping.

Selective routing is curated in advance, not learned by the model. Any measured benefit includes that routing advantage; this is not an evaluation of automatic skill selection. The full condition deliberately includes more context and is a context strategy comparison, not necessarily the most efficient real-world client configuration.

Default: 10 cases × 3 conditions × 1 repeat = 30 requests per provider, 60 for both. Each request is bounded to 4,096 output tokens, with a 900-second run budget and 120-second maximum request timeout. Provider-default reasoning effort is used and may differ; the runner does not claim equal reasoning compute. Order is deterministically shuffled with seed 731. No temperature or sampling seed is forced, and outputs may vary.

The default is a smoke run, not a statistically powered comparison. For repeated trials, increase both `--repeats` and `--max-calls` deliberately. A truncated run is not a complete comparison. Repeats on the same small set are correlated; avoid treating them as new independent tasks.

## What is measured

- Exact next-action correctness and required/allowed check selection.
- JSON/schema failures and unsafe proposed decisions, separately.
- Errors and incomplete output, retained in attempt denominators.
- Per-request elapsed latency and provider-reported usage, when returned.
- Total reported tokens and tokens per passing response, including failed graded responses.
- Requested/returned model IDs, provider response IDs, prompt hashes, skill-file hashes, dataset hash, runner hash, and request configuration.

An unsafe decision means the model **recommended** an action forbidden by this fixture. It does not mean a production action occurred. Reason text is retained but not semantically graded. The rubric is intentionally narrow and can miss poor reasoning behind a correct answer.

Token counts include reported cache usage where the provider reports it separately. Tokenizers and reasoning-accounting conventions differ across providers; compare context conditions within each provider before interpreting cross-provider totals. Usage is not an invoice: dollar cost is left unknown. If a failed request has no usage data, aggregate token totals are unknown rather than silently excluding it. Latency includes network time and provider processing. No automatic retries are performed.

## Run locally

Requirements: Python 3.10 or newer, network access, access to the requested model, and the corresponding API credential configured securely in the process environment. There are no third-party Python dependencies. Do not commit credentials or put them in a command-line argument.

From the repository root:

```bash
python -m unittest discover -s benchmark -p test_runner.py -v
python benchmark/run.py --provider openai --out benchmark/results/openai-run-002
python benchmark/run.py --provider anthropic --out benchmark/results/anthropic-run-002
```

Every run requires a new output directory to preserve prior evidence. Missing credentials produce a blocked result and exit code 2 without any inference request. A complete run returns 0; transport errors or budget exhaustion return 2 and preserve completed rows. An output cap can produce incomplete model output and must not be counted as a passing case.

The default skill root is the repository root. Use `--skills-root PATH` to compare another checkout; the actual included Markdown files are hashed. `--model` can select a verified account-accessible model ID, but changing it changes the experiment. Do not rename an unavailable model's results to the requested model.

Only synthetic case facts and the repository's skill instructions are sent to the provider. The harness does not send local application source, repository credentials, or the expected-answer fields. Saved records contain the request body but exclude authentication headers. Review generated evidence before publishing it.

## Acceptance and further work

Before a substantive study, freeze the task population, grading rules, meaningful quality and efficiency thresholds, repetition policy, and budgets. Have domain reviewers validate the labels. Add realistic executable workflows and independently protected cases before making production-reliability claims.

Report all conditions even if the skills add tokens or reduce performance. Do not claim RSI convergence from this static, single-turn benchmark. A genuine iterative study must additionally record every proposed change, rejected candidate, evaluation run, and cumulative resource cost.

## Official API/model references

- [GPT-6 Astra model](https://developers.openai.com/api/docs/models/gpt-6-astra): `gpt-6-astra`.
- [OpenAI text generation](https://developers.openai.com/api/docs/guides/text): Responses API.
- [Claude Opus 5.5 model](https://platform.claude.com/docs/en/models/opus-5-5/overview): `claude-opus-5-5`.
- [Claude Messages API](https://platform.claude.com/docs/en/api/messages).

Documentation establishes model identifiers and interface guidance; it does not establish that this account can access either model.


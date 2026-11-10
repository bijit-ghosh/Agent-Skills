# Agent integration and portability

The collection uses portable `SKILL.md` folders. Workflow instructions are independent of the model provider and coding-agent product. Install the same skill source into a location your host discovers; keep its references and scripts together.

## Documented host paths

Paths below were checked against the linked official documentation on 10 November 2026. They describe discovery conventions, not completed end-to-end tests of this collection in each host. Project paths are relative to the **target project**; personal paths use the current user's home directory.

| Agent host | Project destination | Personal destination | Official source |
|---|---|---|---|
| Claude Code | `.claude/skills` | `~/.claude/skills` | [Skills](https://code.claude.com/docs/en/skills) |
| Codex | `.agents/skills` | `~/.agents/skills` | [Build skills](https://learn.chatgpt.com/docs/build-skills) |
| Cursor | `.cursor/skills` | `~/.cursor/skills` | [Agent Skills](https://cursor.com/docs/skills) |
| GitHub Copilot | `.github/skills` | `~/.copilot/skills` | [Agent skills](https://docs.github.com/en/copilot/concepts/customizations/agent-skills) |
| Gemini CLI | `.gemini/skills` | `~/.gemini/skills` | [Agent Skills](https://geminicli.com/docs/cli/skills/) |
| OpenCode | `.opencode/skills` | `~/.config/opencode/skills` | [Skills](https://opencode.ai/docs/skills/) |
| Kiro | `.kiro/skills` | `~/.kiro/skills` | [Agent Skills](https://kiro.dev/docs/skills/) |

Some hosts also recognize shared `.agents/skills` locations. Avoid installing duplicate names into several discovery roots unless you intend to manage precedence. Cloud/remote sessions may not inherit local personal skills; consult the host's documentation and install into the actual execution environment.

For other agents, check whether the installed version supports Agent Skills natively. If it does, use its documented destination. If it only accepts instruction files, ask it to read a selected skill and its relevant local references explicitly. That is manual use, not automatic discovery or a tested native integration. Do not paste the entire catalog into every prompt.

## Install selected skills

Clone this repository, then run the local Python 3.10+ installer. Choose a destination from the table; the installer does not hard-code a client or require a model API.

```bash
git clone https://github.com/bijit-ghosh/Agent-Skills.git
cd Agent-Skills
python scripts/validate.py
python scripts/install.py --dest ~/.cursor/skills software-factory-routing software-factory-implementation software-factory-review
```

For project scope, pass the full path to the target project's skill directory instead of installing into this collection's checkout:

```bash
python scripts/install.py --dest /path/to/your-project/.github/skills software-factory-specification software-factory-evals
```

Windows PowerShell example:

```powershell
python scripts/install.py --dest 'C:\Projects\YourApp\.gemini\skills' software-factory-context software-factory-improvement
```

The installer copies whole folders, rejects unknown names, refuses existing destinations, and rolls back folders it created if copying fails. It does not configure model access, enable tools, edit host settings, or update an existing installation silently. Use [catalog.json](../catalog.json) for available names and [installation sets](../README.md#choose-an-installation-set) for suggested groupings.

In Codex, the optional built-in installer remains an alternative:

```text
$skill-installer install https://github.com/bijit-ghosh/Agent-Skills/tree/main/software-factory-routing
```

The reference repository also offers native plugins and command wrappers. This collection currently distributes standalone skills, not those plugins. Do not substitute this repository's URL into an upstream plugin command: matching plugin manifests are not shipped here.

## Host and model are separate choices

- **Host:** discovers skills, assembles context, exposes tools, applies permissions, and records execution.
- **Model/provider:** supplies reasoning and generation through that host.
- **Skill:** describes a scoped workflow and its evidence requirements.
- **Project tools:** execute tests, builds, browser checks, deployment, and telemetry queries.

Changing the provider does not require rewriting the workflow. It does require validating behavior with the chosen model, tool access, context limits, and host configuration. The bundled benchmark has only OpenAI and Anthropic API adapters; that adapter coverage is narrower than skill portability.

## Minimal host integration contract

1. Discover `SKILL.md` metadata and load the selected skill body when needed.
2. Resolve referenced files relative to that skill's folder.
3. Use the host's existing permissions and the user's authorized scope for tools.
4. Supply the target project's test/build/runtime tools; Python 3.10+ is needed for this collection's utilities.
5. Preserve candidate, case, grader, environment and run identities in evidence.
6. Report unsupported capabilities as unavailable, never as successful checks.

`agents/openai.yaml` is optional Codex display metadata. Other hosts do not need to interpret it to read the workflow. There are no required provider-specific instructions in the skill entrypoints.

## Verify adoption in your environment

After installation, confirm that the intended skill appears or can be explicitly loaded. Run a bounded representative task with synthetic or approved data, verify that local references resolve, inspect actual tool actions and artifacts, and record host/model/version and test limits. Check that a review-only request does not mutate code and that a missing tool produces an honest limitation.

Use [task examples](EXAMPLES.md) and [behavioral scenarios](../evals/README.md). Successful folder copying and repository CI validate packaging and utilities; they do not establish skill effectiveness in a particular host.

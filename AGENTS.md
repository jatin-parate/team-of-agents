# Agent instructions

## Project purpose

This repository packages the `tech-lead-orchestrator` skill as an installable plugin for Claude Code, Codex, and Kiro, with platform-specific companion agent definitions. Claude Code loads plugin agents from `agents/*.md`; Codex agents are TOML; Kiro agents are JSON in `.kiro/agents/`. See `README.md` for each platform's install flow.

## Working in this repository

- Keep changes focused on the plugin, its orchestration skill, companion agent definitions, or their documentation.
- Keep `plugin.json` and `.agents/plugins/marketplace.json` consistent when changing plugin identity or metadata.
- Keep `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` identities consistent. Keep Claude agent Markdown files in `agents/` aligned with the role instructions in the Codex TOML definitions, including the role boundaries and test ownership.
- Do not claim Codex agents are available after Codex plugin installation alone: the TOML definitions must be copied to the user's Codex agent directory, then Codex restarted. Claude Code plugin installation registers the Markdown agents in `agents/`. Kiro profiles in `.kiro/agents/` load when this repo is open as a workspace; importing the Power alone does not register them. The `setup-kiro-subagents` skill copies bundled profiles into another project's `.kiro/agents/` directory on request.
- Keep platform model settings separate: Codex agent TOMLs use `gpt-6-luna`; Kiro agent profiles use `claude-haiku-5.5`; Claude Code agents inherit the active session model.
- Keep the Kiro profiles in `.kiro/agents/` aligned with their bundled copies in `skills/setup-kiro-subagents/references/kiro-agents/` and with the approved roster in `skills/tech-lead-orchestrator/SKILL.md`.
- Keep agent definitions and skill instructions aligned. In particular, preserve role boundaries, test ownership, and the orchestrator's no-direct-implementation boundary. The `documentation-writer` may explore code and edit Markdown documentation only; for documentation work, the orchestrator should use `code-explorer` to identify touchpoints and repository documentation guidance before assigning bounded slices.
- Do not add machine-specific paths as if they were portable defaults. Clearly identify paths users must configure locally.
- Do not add dependencies or generated files for this documentation/configuration-only project without a clear need.

## Validation

There is no application build or test suite in this repository. For changes to manifests or agent definitions, validate JSON and TOML syntax with the standard library:

```sh
python3 - <<'PY'
import json
import tomllib
from pathlib import Path

for path in (
    Path("plugin.json"),
    Path(".agents/plugins/marketplace.json"),
    Path(".claude-plugin/plugin.json"),
    Path(".claude-plugin/marketplace.json"),
):
    json.loads(path.read_text())
for path in Path("agents").glob("*.toml"):
    tomllib.loads(path.read_text())
for path in Path(".kiro/agents").glob("*.json"):
    json.loads(path.read_text())
for path in Path("skills/setup-kiro-subagents/references/kiro-agents").glob("*.json"):
    json.loads(path.read_text())
print("JSON and TOML syntax OK")
PY
```

For documentation changes, check that referenced paths and commands match the repository layout and that Markdown links and code blocks are valid.
For Claude Code plugin or agent changes, run `claude plugin validate .` when the Claude Code CLI is available; it validates manifest and agent frontmatter.

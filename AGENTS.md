# Agent instructions

## Project purpose

This repository packages the `tech-lead-orchestrator` skill as a portable Agent Plugin for Codex and Kiro, with companion Codex and Kiro custom-agent definitions. The plugin installs the skill only. Codex agents are installed separately; Kiro profiles are loaded from `.kiro/agents/` when this repo is opened as a workspace. See `README.md`.

## Working in this repository

- Keep changes focused on the plugin, its orchestration skill, companion agent definitions, or their documentation.
- Keep `plugin.json` and `.agents/plugins/marketplace.json` consistent when changing plugin identity or metadata.
- Do not claim that companion agents are available after Power/plugin installation alone. The Codex TOML definitions must be copied to the user's Codex agent directory, then Codex restarted. Kiro profiles in `.kiro/agents/` load when this repo is opened as a workspace; importing the Power alone does not register them. The `setup-kiro-subagents` skill copies bundled profiles into another project's `.kiro/agents/` directory on request.
- Keep platform model settings separate: Codex agent TOMLs use `gpt-6-luna`; Kiro agent profiles use `claude-haiku-5.5`.
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

for path in (Path("plugin.json"), Path(".agents/plugins/marketplace.json")):
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

# Agent instructions

## Project purpose

This repository packages the `tech-lead-orchestrator` skill as a portable Agent Plugin for Codex and Kiro and provides companion Codex custom-agent definitions. The plugin does not install or register those custom agents; users install them separately as described in `README.md`.

## Working in this repository

- Keep changes focused on the plugin, its orchestration skill, companion agent definitions, or their documentation.
- Keep `plugin.json` and `.agents/plugins/marketplace.json` consistent when changing plugin identity or metadata.
- Do not claim that companion agents are available after plugin installation. The TOML definitions are for Codex and must be copied to the user's Codex agent directory, then Codex restarted. Kiro Power installation installs the portable skill only; equivalent Kiro custom agents must be configured separately.
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
print("JSON and TOML syntax OK")
PY
```

For documentation changes, check that referenced paths and commands match the repository layout and that Markdown links and code blocks are valid.

# Team of Agents

A Codex plugin that packages the `tech-lead-orchestrator` skill, with companion Codex custom-agent definitions in `agents/`.

## Install the plugin

From the cloned repository, add its marketplace and install the plugin:

```sh
codex plugin marketplace add .
codex plugin install team-of-agents@team-of-agents
```

The plugin makes the bundled skill available to Codex. Try: “Use the tech-lead-orchestrator skill to plan this engineering task.”

## Install the companion agents

Codex plugins do not currently register custom agent TOML files. To use these definitions as subagents, copy them into your user agent directory:

```sh
mkdir -p ~/.codex/agents
cp agents/*.toml ~/.codex/agents/
```

Restart Codex after copying. The `backend-senior-engineer` and `test-writer` definitions also refer to a separately installed TDD skill at `/Users/jparate/.agents/skills/tdd/SKILL.md`; update those `skills.config` paths to your local TDD skill location before using them elsewhere.

## Repository layout

- `plugin.json`: portable plugin manifest.
- `.agents/plugins/marketplace.json`: repo marketplace catalog.
- `skills/`: skills bundled into the plugin.
- `agents/`: companion Codex custom-agent definitions (manual installation).

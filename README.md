# Team of Agents

A portable Agent Plugin that packages the `tech-lead-orchestrator` skill for Codex and Kiro. The repo also includes companion Codex custom-agent definitions in `agents/`.

## Install in Kiro

You can import the Power from GitHub or from a local clone:

- **GitHub:** In Kiro, open **Powers** → **Add Custom Power** → **Import power from GitHub**, then enter `https://github.com/jatin-parate/team-of-agents`.
- **Local clone:** Open the repository root in Kiro, then choose **Powers** → **Add Custom Power** → **Import power from a folder** and select the repository root.

After installation, start a new chat and ask: “Use the tech-lead-orchestrator skill to plan this engineering task.”

This installs the portable skill as a Kiro Power. Kiro Power installation does not install Codex agent TOML files; those definitions are only for Codex. The orchestration instructions rely on specialist subagents, so Kiro users need equivalent Kiro custom agents configured separately if they want the full delegated workflow.

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

Restart Codex after copying. The `backend-senior-engineer` and `test-writer` definitions also refer to a separately installed TDD skill at `/Users/jparate/.agents/skills/tdd/SKILL.md`; update those `skills.config` paths to your local TDD skill location before using them elsewhere. The `documentation-writer` agent explores an assigned feature slice and writes Markdown documentation only.

## Working with coding agents

See [`AGENTS.md`](AGENTS.md) for repository-specific guidance and validation steps. Marketplace installation makes the orchestration skill available; it does not install the companion agents. Copy the agent definitions separately, then restart Codex before asking the skill to delegate work.

## Repository layout

- `plugin.json`: portable plugin manifest.
- `.agents/plugins/marketplace.json`: repo marketplace catalog.
- `skills/`: skills bundled into the plugin.
- `agents/`: companion Codex custom-agent definitions (manual installation).

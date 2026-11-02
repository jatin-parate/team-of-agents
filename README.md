# Team of Agents

A portable Agent Plugin that packages the `tech-lead-orchestrator` skill for Codex and Kiro. The repo also includes companion Codex custom-agent definitions in `agents/`.

## Install in Kiro

You can import the Power from GitHub or from a local clone:

- **GitHub:** In Kiro, open **Powers** → **Add Custom Power** → **Import power from GitHub**, then enter `https://github.com/jatin-parate/team-of-agents`.
- **Local clone:** Open the repository root in Kiro, then choose **Powers** → **Add Custom Power** → **Import power from a folder** and select the repository root.

After installation, start a new chat and ask: “Use the tech-lead-orchestrator skill to plan this engineering task.”

The Power installs skills, not custom-agent profiles. If you installed the Power into another project and the specialist agents are missing, open that project in Kiro and run `/setup-kiro-subagents`. The skill copies this Power's six specialist profiles into the workspace's `.kiro/agents/` folder. Trust the workspace and start a new chat before delegating. When you open this repository itself as the workspace, Kiro loads the profiles directly from `.kiro/agents/`.

All Kiro profiles use Claude Haiku 5.5. Kiro currently marks Haiku 5.5 experimental and limits availability by plan and region. If it is unavailable, choose an available model in Kiro or change the `model` field in `.kiro/agents/`. See [Kiro model availability](https://kiro.dev/docs/models/available-models/).

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

The Codex agent definitions continue to use `gpt-6-luna`; Kiro's separate profiles use Claude Haiku 5.5.

## Working with coding agents

See [`AGENTS.md`](AGENTS.md) for repository-specific guidance and validation steps. Marketplace installation makes the orchestration skill available; it does not install the companion agents. Copy the agent definitions separately, then restart Codex before asking the skill to delegate work.

## Repository layout

- `plugin.json`: portable plugin manifest.
- `.agents/plugins/marketplace.json`: repo marketplace catalog.
- `skills/`: skills bundled into the plugin.
- `agents/`: companion Codex custom-agent definitions (manual installation).
- `.kiro/agents/`: Kiro project custom-agent profiles.
- `skills/setup-kiro-subagents/`: Power skill that installs the specialist profiles into another Kiro workspace.

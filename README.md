# Team of Agents

A portable Agent Plugin that packages the `tech-lead-orchestrator` skill for Claude Code, Codex, Kiro, and Pi. It also includes platform-specific companion agent definitions.

## Install in Claude Code

From a Claude Code terminal session, add the repository marketplace and install the plugin:

```sh
claude plugin marketplace add jatin-parate/team-of-agents
claude plugin install team-of-agents@team-of-agents
```

Start a new session and invoke `/team-of-agents:tech-lead-orchestrator`. The plugin also registers the specialist agents under the `team-of-agents:` namespace; the skill delegates to names such as `team-of-agents:backend-senior-engineer`.

To check the installation, run `claude plugin list`. The installed plugin includes the skill and six Claude Code subagents.

## Install in Kiro

You can import the Power from GitHub or from a local clone:

- **GitHub:** In Kiro, open **Powers** → **Add Custom Power** → **Import power from GitHub**, then enter `https://github.com/jatin-parate/team-of-agents`.
- **Local clone:** Open the repository root in Kiro, then choose **Powers** → **Add Custom Power** → **Import power from a folder** and select the repository root.

After installation, start a new chat and ask: “Use the tech-lead-orchestrator skill to plan this engineering task.”

The Power installs skills, not custom-agent profiles. If you installed the Power into another project and the specialist agents are missing, open that project in Kiro and run `/setup-kiro-subagents`. The skill copies this Power's six specialist profiles into the workspace's `.kiro/agents/` folder. Trust the workspace and start a new chat before delegating. When you open this repository itself as the workspace, Kiro loads the profiles directly from `.kiro/agents/`.

All Kiro profiles use Claude Haiku 5.5. Kiro currently marks Haiku 5.5 experimental and limits availability by plan and region. If it is unavailable, choose an available model in Kiro or change the `model` field in `.kiro/agents/`. See [Kiro model availability](https://kiro.dev/docs/models/available-models/).

## Install in Pi

Install this repository as a Pi package:

```sh
pi install git:github.com/jatin-parate/team-of-agents
```

Start a new Pi session and run `/skill:setup-pi-agents`. The setup skill installs the `pi-subagents` package that provides Pi's subagent tool. This repository package then supplies Pi-specific profiles for its six specialist agents. Restart Pi or run `/reload`, then ask Pi to use an agent such as `code-explorer` or `backend-senior-engineer`. You can also invoke `/skill:tech-lead-orchestrator` directly.

This setup requires Pi 1.2.0 or newer.

Pi agent profiles are in `agents/pi/`; the Codex TOML, Claude Code Markdown, and Kiro JSON profiles are not loaded by Pi. Review package sources before installing them because Pi packages can include executable extensions.

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

See [`AGENTS.md`](AGENTS.md) for repository-specific guidance and validation steps. Claude Code plugin installation includes the skill and subagents. Codex plugin installation provides the skill only; copy the agent TOML files separately and restart Codex. Kiro Power installation also provides the skill only; use `/setup-kiro-subagents` in the target workspace to install the Kiro profiles. Pi package installation provides its skill and Pi-specific profiles; use `/skill:setup-pi-agents` to install Pi's subagent tool.

## Repository layout

- `plugin.json`: portable plugin manifest.
- `.agents/plugins/marketplace.json`: repo marketplace catalog.
- `.claude-plugin/`: Claude Code plugin and marketplace manifests.
- `package.json`: Pi package manifest, exposing the skills directory.
- `skills/`: skills bundled into the plugin.
- `agents/`: companion Codex TOML and Claude Code Markdown agent definitions.
- `agents/pi/`: Pi-specific subagent profiles.
- `.kiro/agents/`: Kiro project custom-agent profiles.
- `skills/setup-kiro-subagents/`: Power skill that installs the specialist profiles into another Kiro workspace.

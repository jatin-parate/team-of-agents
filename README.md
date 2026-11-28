# Team of Agents

A portable Agent Plugin that packages the `tech-lead-orchestrator` and `tech-lead-planner` skills for Claude Code, Codex, Kiro, and Pi. It also includes platform-specific companion agent definitions.

The backend and frontend senior engineers implement their respective production-code scopes and unit tests. The test writer owns integration tests for implementation work. When explicitly requested, the backend dev-tester runs targeted API automation against the locally running service, reusing existing suites or adding tests as needed. If startup fails, it can ask you to run the service and provide its port.

For a planning-only session, invoke `tech-lead-planner` with a ticket and target repository. It delegates discovery and produces a plan directory containing requirements, clarifications, design, independent critique, incremental tasks, and verification and rollout guidance. An architecture specialist proposes a design, and a separate critic seeks evidence-based failure modes and documents their disposition. By default it uses `plans/<ticket-id-or-short-slug>/`; provide another path if preferred. When ticket systems, external documentation, or scoped operational evidence are relevant, the `planning-researcher` is instructed to gather them read-only using available authorized tools and configured access. Shell-capable profiles rely on host permissions and the active identity to enforce access; the profile itself does not prevent write commands, install integrations, or grant access. The architecture and critic profiles also rely on instructions and host permissions for their read-only boundaries; Kiro gives them shell access for bounded searches. It assesses frontend and backend scope by default, tracks missing UI design evidence, and plans cross-stack work when required. When the user answers questions or requests revisions, it reconciles affected deliverables, removes resolved items from the open-question list, and provides a concise guide to what changed and what to review. It stops before implementation. In a later session, give the directory and selected task to `tech-lead-orchestrator`, which revalidates relevant context before proceeding. The same specialist profiles and platform setup described below are required.

## Continue work in a fresh session

Use the bundled **save-progress** prompt before leaving a task. It delegates a compact checkpoint to `.team-of-agents/progress/<task-slug>.md` in the target workspace, or to another shared durable Markdown path you provide. In a fresh session, use **resume-progress**, optionally supplying that path or task name. The lead loads the appropriate skill, delegates revalidation, and gives new specialists a fresh context map. If several unfinished tasks match, it asks you to choose. A planning checkpoint resumes planning; request implementation separately.

The commands are invoked explicitly; progress is not saved automatically at each milestone. Save again whenever you need an updated snapshot. If saving fails or work is still running, the lead reports the limitation. The checkpoint is local workspace content that could be committed or shared, so review it for sensitive information. For another machine or provider, make the checkpoint, referenced plans, and relevant workspace changes available there first.

Available entry points:

- **Claude Code:** Plugin installation registers `/team-of-agents:save-progress` and `/team-of-agents:resume-progress` from `commands/`.
- **Pi:** The package registers `/save-progress` and `/resume-progress` as prompt templates. Reload Pi after updating the package.
- **Kiro CLI:** Copy `prompts/save-progress.md` and `prompts/resume-progress.md` from a clone into the target workspace's `.kiro/prompts/`. In CLI V3 invoke `/save-progress` or `/resume-progress`; other CLI harnesses support `@save-progress` and `@resume-progress`. Kiro Power installation alone does not install these prompt files.
- **GitHub Copilot:** In a supported IDE, copy the two files to the target workspace's `.github/prompts/`, renaming them `save-progress.prompt.md` and `resume-progress.prompt.md`, then select the desired prompt in chat. Prompt file support varies by client; for Copilot CLI, include the relevant file as context instead.
- **Codex:** Refer to the appropriate prompt file from an accessible clone in your message and ask Codex to follow it, for example: “Follow `@/path/to/team-of-agents/prompts/save-progress.md`.” Replace the path with your clone's actual path. The plugin does not register these prompt files as Codex slash commands.

These are prompt-driven snapshots, not host startup hooks or guarantees that child processes can be restored. Earlier facts and check results can become stale, so the team verifies relevant state. Loading the skill, checkpoint and necessary files still uses tokens; cost and cache behavior depend on the host, model and billing plan. Avoiding the full old transcript may reduce context, but does not guarantee savings. The Claude command copies and the Pi prompt templates contain the same instructions; keep both pairs in sync when editing.

## Install in Claude Code

From a Claude Code terminal session, add the repository marketplace and install the plugin:

```sh
claude plugin marketplace add jatin-parate/team-of-agents
claude plugin install team-of-agents@team-of-agents
```

Start a new session and invoke `/team-of-agents:tech-lead-orchestrator`. The plugin also registers the specialist agents under the `team-of-agents:` namespace; the skill delegates to names such as `team-of-agents:backend-senior-engineer`.

To check the installation, run `claude plugin list`. The installed plugin includes the skill and eleven Claude Code subagents.

When enabled, the plugin's `SubagentStart` hook reinforces the five-turn and `node_modules` limits for `code-explorer`; the agent's `maxTurns` setting enforces the turn cap.

## Install in Kiro

You can import the Power from GitHub or from a local clone:

- **GitHub:** In Kiro, open **Powers** → **Add Custom Power** → **Import power from GitHub**, then enter `https://github.com/jatin-parate/team-of-agents`.
- **Local clone:** Open the repository root in Kiro, then choose **Powers** → **Add Custom Power** → **Import power from a folder** and select the repository root.

After installation, start a new chat and ask: “Use the tech-lead-orchestrator skill to plan this engineering task.”

The Power installs skills, not custom-agent profiles. If you installed the Power into another project and the specialist agents are missing, open that project in Kiro and run `/setup-kiro-subagents`. The skill copies this Power's eleven specialist profiles into the workspace's `.kiro/agents/` folder. Trust the workspace and start a new chat before delegating. When you open this repository itself as the workspace, Kiro loads the profiles directly from `.kiro/agents/`.

The Kiro backend-dev-tester profile uses Claude Sonnet 5.5; the other Kiro profiles use Claude Haiku 5.5. Kiro currently marks Haiku 5.5 experimental and limits availability by plan and region. If it is unavailable, choose an available model in Kiro or change the `model` field in `.kiro/agents/`. See [Kiro model availability](https://kiro.dev/docs/models/available-models/).

## Install in Pi

Install this repository as a Pi package:

```sh
pi install git:github.com/jatin-parate/team-of-agents
```

Start a new Pi session and run `/skill:setup-pi-agents`. The setup skill installs the `pi-subagents` package that provides Pi's subagent tool. This repository package then supplies Pi-specific profiles for its eleven specialist agents. Restart Pi or run `/reload`, then ask Pi to use an agent such as `code-explorer`, `backend-senior-engineer`, or `frontend-senior-engineer`. You can also invoke `/skill:tech-lead-orchestrator` directly.

This setup requires Pi 1.2.0 or newer.

Pi agent profiles are in `agents/pi/`; the Codex TOML, Claude Code Markdown, and Kiro JSON profiles are not loaded by Pi. Review package sources before installing them because Pi packages can include executable extensions.

### Pi assistant telemetry

The local helper combines assistant message events from a parent session JSONL and its immediate child logs matching `*/run-0/session.jsonl`. It keeps the first record for each top-level event `id`, orders the output by timestamp, and writes JSONL to stdout.

Add an alias to your shell configuration, replacing the path with your local clone:

```sh
export TEAM_OF_AGENTS_DIR="/path/to/team-of-agents"
alias pi-assistant-telemetry='python3 "$TEAM_OF_AGENTS_DIR/scripts/pi-assistant-telemetry.py"'
```

Run it with the parent JSONL path and the directory that contains its child run directories:

```sh
pi-assistant-telemetry /path/to/parent-session.jsonl /path/to/parent-session-directory
```

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

The Codex agent definitions use `gpt-6-luna`. The backend dev-tester uses Sonnet in Claude Code, Kiro, and Pi; Kiro's other profiles use Haiku.

## Working with coding agents

See [`AGENTS.md`](AGENTS.md) for repository-specific guidance and validation steps. Claude Code plugin installation includes the skill and subagents. Codex plugin installation provides the skill only; copy the agent TOML files separately and restart Codex. Kiro Power installation also provides the skill only; use `/setup-kiro-subagents` in the target workspace to install the Kiro profiles. Pi package installation provides its skill and Pi-specific profiles; use `/skill:setup-pi-agents` to install Pi's subagent tool.

## Repository layout

- `plugin.json`: portable plugin manifest.
- `.agents/plugins/marketplace.json`: repo marketplace catalog.
- `.claude-plugin/`: Claude Code plugin and marketplace manifests.
- `hooks/`: Claude Code plugin lifecycle hooks.
- `package.json`: Pi package manifest, exposing the skills directory.
- `scripts/`: Claude hook and local Pi telemetry helpers.
- `skills/`: skills bundled into the plugin.
- `agents/`: companion Codex TOML and Claude Code Markdown agent definitions.
- `agents/pi/`: Pi-specific subagent profiles.
- `.kiro/agents/`: Kiro project custom-agent profiles.
- `skills/setup-kiro-subagents/`: Power skill that installs the specialist profiles into another Kiro workspace.

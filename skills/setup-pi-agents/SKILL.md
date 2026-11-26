---
name: setup-pi-agents
description: Install Pi subagent support and this repository's specialist agent profiles. Use when setting up team-of-agents in Pi or when its subagents are missing.
---

# Set up Team of Agents in Pi

Install the Pi subagent extension and this repository's Pi package so Pi can discover and run the specialist profiles.

1. Check the installed packages with `pi list`.
2. If `npm:pi-subagents` is missing, run:

   ```sh
   pi install npm:pi-subagents
   ```

3. If `git:github.com/jatin-parate/team-of-agents` is missing, run:

   ```sh
   pi install git:github.com/jatin-parate/team-of-agents
   ```

4. If the repository package is already installed and the user asks to update it, run `pi update git:github.com/jatin-parate/team-of-agents`. Update `npm:pi-subagents` separately only when the user asks to update the runner extension.
5. Reload Pi with `/reload`, or restart the session.
6. Confirm the `subagent` tool is available and that the repository agents appear. The profiles are `code-explorer`, `backend-senior-engineer`, `test-writer`, `independent-reviewer`, `qa-tester`, and `documentation-writer`.

If Pi reports a project trust prompt, review the repository and approve it before using project resources. If a package is already installed, do not reinstall it unless the user asks to update it. Do not overwrite local agent definitions; the profiles ship inside the repository's installed Pi package.

`backend-senior-engineer` pins `claude-bridge/claude-sonnet-5-5`. `independent-reviewer` defaults to `claude-bridge/claude-haiku-5-5` for mechanical checks; select Sonnet per invocation for semantic review. `code-explorer`, `qa-tester`, and `test-writer` also pin Haiku 5.5. `documentation-writer` inherits the active Pi session's model. Their prompts preserve the role boundaries in this repository. Some role instructions may refer to tools, skills, or paths that are specific to another agent environment; check availability in Pi and report gaps rather than claiming those dependencies are installed.

The orchestrator requires exact verification commands in the initial context map, authorizes child agents to execute within assigned scope without another approval prompt, and prohibits `git stash` and `git checkout` in delegation instructions. Keep the explorer to five turns and out of `node_modules` unless the parent requests it. For iterative Pi test fixes, reuse the same child run with `details: { runId: ... }`, not `details.missionId`. Do not resume a backend Sonnet run above about 40k context for small diagnostics or unrelated work; use Haiku for temporary diagnostics and a clean Sonnet run for unrelated implementation.

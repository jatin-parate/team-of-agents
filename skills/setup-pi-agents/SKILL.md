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

4. Reload Pi with `/reload`, or restart the session.
5. Confirm the `subagent` tool is available and that the repository agents appear. The profiles are `code-explorer`, `backend-senior-engineer`, `test-writer`, `independent-reviewer`, `qa-tester`, and `documentation-writer`.

If Pi reports a project trust prompt, review the repository and approve it before using project resources. If a package is already installed, do not reinstall it unless the user asks to update it. Do not overwrite local agent definitions; the profiles ship inside the repository's installed Pi package.

The Pi profiles inherit the active Pi session's model. Their prompts preserve the role boundaries in this repository. Some role instructions may refer to tools, skills, or paths that are specific to another agent environment; check availability in Pi and report gaps rather than claiming those dependencies are installed.

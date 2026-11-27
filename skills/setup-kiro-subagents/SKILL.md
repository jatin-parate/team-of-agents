---
name: setup-kiro-subagents
description: Install this Power's Team of Agents specialist profiles into the current Kiro workspace. Use when the Kiro Power is installed but its specialist subagents are missing or unavailable.
---

# Set up Team of Agents subagents in Kiro

Kiro Powers install skills, but they do not register custom-agent profiles. This skill installs the bundled specialist profiles into the current workspace so Kiro can discover them.

1. Confirm the current workspace is the project where the user wants these agents available. Install into that project's `.kiro/agents/` directory, not the global Kiro configuration.
2. Check whether any of these files already exist: `code-explorer.json`, `backend-senior-engineer.json`, `frontend-senior-engineer.json`, `test-writer.json`, `independent-reviewer.json`, `qa-tester.json`, `backend-dev-tester.json`, `documentation-writer.json`, `planning-researcher.json`, `architecture-specialist.json`, and `plan-critic.json`.
3. If a destination exists, do not overwrite it. Report the conflicting paths and ask before replacing or merging them.
4. Create `.kiro/agents/` if needed, then copy the matching JSON files from this skill's `references/kiro-agents/` directory into it without changes.
5. Confirm the eleven profiles are present and remind the user to trust the workspace and start a new Kiro chat before delegating.

The backend-dev-tester profile uses Claude Sonnet 5.5; the other profiles use Claude Haiku 5.5. Model availability depends on the user's plan and region. If a model is unavailable, have the user select an available model in Kiro or update the profiles' `model` fields.

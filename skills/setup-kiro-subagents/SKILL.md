---
name: setup-kiro-subagents
description: Install this Power's Team of Agents specialist profiles into the current Kiro workspace. Use when the Kiro Power is installed but its specialist subagents are missing or unavailable.
---

# Set up Team of Agents subagents in Kiro

Kiro Powers install skills, but they do not register custom-agent profiles. This skill installs the bundled specialist profiles into the current workspace so Kiro can discover them.

1. Confirm the current workspace is the project where the user wants these agents available. Install into that project's `.kiro/agents/` directory, not the global Kiro configuration.
2. Check whether any of these files already exist: `code-explorer.json`, `backend-senior-engineer.json`, `test-writer.json`, `independent-reviewer.json`, `qa-tester.json`, and `documentation-writer.json`.
3. If a destination exists, do not overwrite it. Report the conflicting paths and ask before replacing or merging them.
4. Create `.kiro/agents/` if needed, then copy the matching JSON files from this skill's `references/kiro-agents/` directory into it without changes.
5. Confirm the six profiles are present and remind the user to trust the workspace and start a new Kiro chat before delegating.

The profiles use Claude Haiku 5.5. Kiro currently marks that model experimental and availability depends on the user's plan and region. If the model is unavailable, have the user select an available model in Kiro or update the profiles' `model` fields.

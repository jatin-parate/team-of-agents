---
description: Save a portable checkpoint for the current task.
---

Save a compact, durable checkpoint for the current task so a fresh session can continue it. Do not resume or start other work. Follow the active lead skill's delegation, role boundaries, permissions, and user instructions. If acting as a lead that cannot read or write files, delegate discovery to `code-explorer` and checkpoint writing to `documentation-writer`; use a separate handoff note and the existing context-map and dispatch rules. Other agents report to the lead and must not concurrently edit the checkpoint.

Use the user-specified shared durable Markdown path, or `.team-of-agents/progress/<task-slug>.md` under the target workspace. Choose a stable slug and do not overwrite another task's checkpoint or unrelated user content. Confirm the location follows repository guidance and is accessible to the agents. Do not use temporary directories, a child session ID, or a context map as the sole checkpoint.

Collect available child reports. Record running, interrupted, or unknown work as unverified, including its owner and possible partial changes; do not claim it completed. Write about 150 lines at most, including: format version 1; task slug and goal; workspace identity and branch or revision if verified; authorized scope, exclusions and constraints; phase and task statuses with owners; decisions and unresolved questions; changed paths and evidence; exact checks and results or not run; open review and QA findings, blockers and risks; durable plan and artifact paths; and the next bounded action. Distinguish verified facts from claims and historical results. Link to existing plan task files rather than copying them. Do not include credentials, secrets, full transcripts, or source dumps.

Update the existing checkpoint only for the same task. Report the saved path, unfinished or potentially running work, and next action. If the write fails, report the failure and the latest known state; never claim it was saved. Explain that the file is workspace content and could be committed or shared. Stop after saving; do not start a new session or assume a paused child can be restored.

import { stdin } from "node:process";

let input = "";
for await (const chunk of stdin) input += chunk;

try {
  const event = JSON.parse(input);
  if (event.agent_type !== "team-of-agents:code-explorer") process.exit(0);

  process.stdout.write(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: "SubagentStart",
      additionalContext: "Explorer scope: finish within five turns; the profile's maxTurns limit is authoritative. Do not inspect node_modules unless the parent explicitly requests it. Read root package.json scripts, .github/workflows/*.yml, and repository test instructions to record exact test, lint, format, build, and type-check commands, or mark them unavailable. Write the baseline map and stop; append a verified implementation delta only when the parent requests it."
    }
  }));
} catch (error) {
  process.stderr.write(`Invalid hook input: ${error.message}\n`);
  process.exitCode = 1;
}

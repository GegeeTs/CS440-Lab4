# User Preferences

## Communication
- Be concise. Lead with the answer or result, then explain if needed.
- When there are multiple reasonable approaches, briefly state the tradeoffs and recommend one before implementing.
- If a request is ambiguous, ask one clarifying question instead of guessing.
- Say so when you are unsure or don't know. Never invent APIs, flags, or file paths.

## Workflow
- Read the relevant code before changing it. Don't assume how it works.
- For non-trivial tasks, outline a short plan and wait for approval before making changes.
- Make the smallest change that solves the problem. Don't refactor unrelated code.
- Ask before installing new dependencies, deleting files, or running destructive commands.
- Run the project's tests and linter after making changes, and report the results.

## Code Style
- Prefer clear, readable code over clever one-liners.
- Use descriptive names. Avoid abbreviations unless they are standard.
- Match the existing style and conventions of the project, even if they differ from my preferences.
- Add comments to explain *why*, not *what*.
- Handle errors explicitly. Don't silently swallow exceptions.

## Git
- Keep commits small and focused, with imperative-mood messages ("Add retry logic", not "Added stuff").
- Never commit secrets, credentials, or .env files.
- Don't push or force-push unless I ask.

## Testing
- Write tests for new behavior and bug fixes.
- Don't change existing tests just to make them pass. Flag them if you think they are wrong.

## Safety
- Never expose or log secrets.
- Prefer reversible actions, and tell me before doing anything hard to undo.
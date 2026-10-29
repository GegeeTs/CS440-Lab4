# Context Engineering Strategy 1: Write

CS440 - Artificial Intelligence
Colorado State University
Fall 2026

## Overview

This directory demonstrates Strategy 1: Write (Persistent Memory Architecture) using Claude Code.

The goal is to provide an AI coding agent with persistent project context through Markdown files.

Instead of repeatedly explaining the vacuum robot environment and requirements, we store important
information in files that Claude can reference across conversations.

## Problem Description

The vacuum robot operates in a 4x4 grid.

| start | 0  | 0 | 0  |
|-------|----|---|----|
| 0     | X  | 0 | 0  |
| 0     | 0  | 0 | 0  |
| 0     | -1 | 0 | 10 |

The robot will eventually use Q-learning.

The transition model (T) and reward model (R) are not fully provided.

Q-learning is not implemented in this lab.

## Project Structure

```text
write/
├── CLAUDE.md
├── README.md
├── context/
|   ├── environment.md
|   ├── requirements.md
|   └── decisions.md
└── example-user-memory
    └── CLAUDE.md
```

## File Descriptions

### CLAUDE.md

Contains the main instructions for Claude Code.

It also references the supporting context files using the @ import syntax.

### context/environment.md

Documents the vacuum robot's grid, important locations, and unknown environment details.

### context/requirements.md

Documents the current assignment requirements, restrictions, and submission instructions.

### context/decisions.md

Stores important decisions made by the group.

This allows project decisions to be referenced across conversations.

### example-user-memory/CLAUDE.example.md

This document contains general preferences most people would like to have, not specifics about this lab.

To use it, put the contents in your user memory by running `cp example-user-memory/CLAUDE.example.md ~/.claude/CLAUDE.md` file, or if you already have your own user memory set up, use that one. This file is not read by the agent unless it is explicitly told to or the content is in `~/.claude/CLAUDE.md`.

## How the Strategy Works

Claude Code uses CLAUDE.md as persistent project-level instructions.

CLAUDE.md imports additional Markdown files containing project context.

These files provide reusable information about:

- The environment
- The assignment requirements
- The group's decisions

Because this information is stored in files, it can be referenced in future conversations without manually repeating it.

## Demonstration

1. Open a terminal in the write directory.
2. Start Claude Code.
3. Ask Claude about the vacuum robot environment.
4. Verify its response against environment.md.
5. Ask Claude about the assignment requirements.
6. Verify its response against requirements.md.
7. Start a new Claude Code conversation.
8. Ask the same questions without providing
   the environment or requirements again.
9. Verify that Claude still uses the persistent
   project context.

## Expected Behavior

Claude should:

- Correctly describe the 4x4 grid.
- Identify the starting position and obstacle.
- Identify the -1 and +10 cells.
- Recognize that T and R are not fully provided.
- Know that Q-learning is planned for later.
- Follow the current no-code restriction.

## Why This Is Context Engineering

The Write strategy stores important project information outside the active conversation.

This reduces the need for users to repeatedly provide the same information.

It also helps maintain consistency between different Claude Code sessions.

## Limitations

Persistent context must be maintained.

If project requirements change, the relevant Markdown files must be updated.

Storing information in a file does not guarantee that every instruction will always be followed.
The agent's responses should still be verified.
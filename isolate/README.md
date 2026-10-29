# Context Engineering Strategy 4: Isolate

CS440 - Artificial Intelligence
Colorado State University
Fall 2026

## Overview

This directory demonstrates Strategy 4: Isolation via Subagents using Claude Code.

A main agent splits the work and gives each part to a specialist. Each specialist receives only the context needed for its task and returns a short summary.

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
isolate/
├── CLAUDE.md
├── README.md
├── context/
│   ├── environment.md
│   └── requirements.md
└── .claude/
    └── agents/
        ├── environment-specialist.md
        ├── requirements-specialist.md
        └── configuration-reviewer.md
```

## File Descriptions

### CLAUDE.md

Contains the main instructions, specialist assignments, and delegation rules.

### context/environment.md

Documents the vacuum robot's grid, important locations, and unknown environment details.

### context/requirements.md

Documents the assignment scope and submission requirements.

### .claude/agents/environment-specialist.md

Defines the specialist that checks the grid and identifies unknown environment details.

### .claude/agents/requirements-specialist.md

Defines the specialist that checks the assignment scope and submission requirements.

### .claude/agents/configuration-reviewer.md

Defines the specialist that reviews selected configuration files for errors and contradictions.

## How the Strategy Works

1. You give Claude Code a task.
2. Claude reads CLAUDE.md and selects the appropriate specialists.
3. Each specialist receives a focused task and the relevant sources, rather than the full chat history.
4. Each specialist returns a short summary.
5. The main agent combines the findings into an answer.

All three specialists are read-only.

## Demonstration

1. Open a terminal in the isolate directory and start Claude Code.
2. Run `/agents` to check that the three specialists appear.
3. Ask Claude to review the grid and assignment requirements using the specialists.
4. Check the actual delegations and compare their responses with the source files.

## Expected Behavior

Claude should:

- Identify the start at (0, 0), obstacle, and reward cells correctly.
- Recognize that T and R are not fully provided.
- Keep Q-learning for a future lab.
- Give each specialist only the context needed for its task.
- Report missing information instead of inventing rules.

## Why This Is Context Engineering

The Isolate strategy separates tasks into focused contexts. This reduces irrelevant information and helps each specialist stay on its assigned task.

## Limitations

File boundaries are instructions, not enforced access restrictions. Responses and actual delegation should still be verified. A live Claude Code demonstration has not yet been tested.

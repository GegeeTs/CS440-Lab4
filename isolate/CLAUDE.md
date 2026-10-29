# Vacuum Robot Project
## Context Engineering Strategy 4: Isolate

You are assisting with a vacuum robot project for CS440, Artificial Intelligence, at Colorado State University.

This folder demonstrates Strategy 4: Isolation via Subagents.

The goal is to give each specialist only the context needed for its task.

## Project Overview

The vacuum robot operates in a 4x4 grid environment.

The environment contains:
- One starting position at the top-left
- One obstacle
- One cell labeled -1
- One goal cell labeled +10
- Normal cells labeled 0

The transition model (T) and reward model (R) are not fully provided.

Q-learning will be implemented in a future lab.

## Project Context

The following files contain important project information:

- `context/environment.md`: grid details and unknown environment rules
- `context/requirements.md`: assignment scope and submission requirements

Pass each file only to the specialist that needs it. Do not import all context into every task.

## Instructions

1. Delegate grid questions to `environment-specialist` with `context/environment.md`.
2. Delegate assignment questions to `requirements-specialist` with `context/requirements.md`.
3. Delegate configuration reviews to `configuration-reviewer` with the specific files and relevant source excerpts.
4. Give each specialist a clear task, allowed files, and expected output. Do not pass the full conversation.
5. Combine their short summaries and identify missing or contradictory information.
6. Do not invent transition probabilities, reward rules, or implementation results.

## Current Lab Scope

This lab focuses on configuring context engineering strategies using Claude Code.

Do not implement Q-learning or write robot implementation code during this lab.

## Specialists

Specialist definitions are stored in `.claude/agents/`.

Each specialist reads only the sources assigned to it and returns a short summary. All specialists are read-only.

Use actual subagent calls. If a specialist cannot run, report that limitation.

Do not modify project files without permission. Leave `../write/` unchanged unless the user requests otherwise.

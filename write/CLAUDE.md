# Vacuum Robot Project
## Context Engineering Strategy 1: Write

You are assisting with a vacuum robot project for CS440, Artificial Intelligence, at Colorado State University.

This repository demonstrates Strategy 1: Write(Persistent Memory Architecture).

The goal is to maintain important project information in persistent Markdown files that Claude Code can reference across conversations.

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

- @context/environment.md
- @context/requirements.md
- @context/decisions.md

Use these files as the project's persistent context.

## Instructions

1. Read and follow the project requirements.
2. Refer to the environment specification when answering questions about the grid.
3. Do not invent missing transition probabilities or reward rules.
4. Distinguish confirmed requirements from assumptions.
5. Consult the project decisions before suggesting changes to previously established choices.
6. If information is missing or contradictory, identify the issue and ask for clarification.
7. Keep responses consistent with the documented environment and requirements.

## Current Lab Scope

This lab focuses on configuring context engineering strategies using Claude Code.

Do not implement Q-learning or write robot implementation code during this lab.

## Persistent Memory

Important project information should be recorded in the appropriate context files.

- Environment details belong in environment.md.
- Assignment requirements belong in requirements.md.
- Team decisions belong in decisions.md.

When a new decision is made, suggest updating decisions.md so the information is available in future conversations.

Do not modify project files without permission.
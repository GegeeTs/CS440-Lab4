# Vacuum Robot Environment

## Overview

The vacuum robot operates in a 4x4 grid environment.

The environment is provided in the CS440 Lab 4 assignment.

## Grid Layout

| start | 0  | 0 | 0  |
|-------|----|---|----|
| 0     | X  | 0 | 0  |
| 0     | 0  | 0 | 0  |
| 0     | -1 | 0 | 10 |

## Coordinate System

For documentation purposes, positions use zero-based (row, column) coordinates.

The top-left cell is (0, 0).

## Important Locations

| Position | Value | Description |
|----------|-------|-------------|
| (0, 0)   | start | Robot's starting position |
| (1, 1)   | X     | Obstacle |
| (3, 1)   | -1    | Negative reward cell |
| (3, 3)   | 10    | Positive reward cell |
| Other    | 0     | Normal cells |

## Environment Characteristics

The environment contains:

- 16 total grid positions
- One obstacle
- One starting position
- One negative reward cell
- One positive reward cell

The robot will eventually use reinforcement learning to learn how to interact with this environment.

## Future Work

A future lab will implement Q-learning.

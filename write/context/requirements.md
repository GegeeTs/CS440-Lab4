# CS440 Lab 4 Requirements

## Assignment

Lab: Vacuum Robot Using Reinforcement Learning

## Objective

Prepare the vacuum robot project using context engineering strategies.

The assignment focuses on:

1. Strategy 1: Write (Persistent Memory)
2. Strategy 4: Isolation via Subagents

This directory implements Strategy 1.

## Environment

The vacuum robot uses the following 4x4 grid:

| start | 0  | 0 | 0  |
|-------|----|---|----|
| 0     | X  | 0 | 0  |
| 0     | 0  | 0 | 0  |
| 0     | -1 | 0 | 10 |

The transition model (T) and reward model (R) are not fully provided.

Q-learning will be implemented later.

## Current Lab Restrictions

This lab focuses on context engineering configuration. Q-learning will be implemented later.

Focus on:
- Context engineering configuration
- Persistent project instructions
- Project documentation
- Demonstrating how Claude Code uses the context

Do not implement Q-learning yet.

## Required Submission

The group must submit the following on Canvas:

### 1. Repository Links

A text file containing the links to the repositories configured for the required strategies.

### 2. README

A README file documenting the project structure and configuration decisions.

### 3. Video Presentation

A video demonstrating the configurations.

Requirements:
- Maximum duration: 3 minutes
- Every group member must participate
- Students must show their faces while presenting
- Use a professional background
- Explain configuration file decisions
- Demonstrate how the configurations address
  the assignment requirements

The video must be private and shared only with the instructor team.

If submitting a video link, put it in group_name.txt for a group submission or firstName_lastName.txt for an individual submission.

Submissions without a video receive zero points.

## AI Policy

The use of AI is allowed for this assignment.

## Strategy 1 Objective

Demonstrate how persistent context files allow Claude Code to retain important project instructions across conversations.

The demonstration should show that Claude can retrieve the environment, requirements, and project decisions without the user repeating
all the information.
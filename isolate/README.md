# isolate/: Context Engineering Strategy 4 (Isolate)

CS440 FA2026, Lab 4: Vacuum robot using reinforcement learning.

This folder sets up the context for an AI coding agent (Claude Code) using
**Strategy 4: Isolation via Sub-Agents**. A main agent splits the work and
hands each part to a specialist sub-agent. Each specialist sees only the
context its job needs. This prevents **context confusion**, where irrelevant
information shares the context window and dilutes the agent's focus.

## The problem

```
start  0   0   0
  0    X   0   0
  0    0   0   0
  0   -1   0  10
```

A vacuum robot must reach +10 while avoiding the -1 trap and the wall (X).
Movement is slippery (80% intended, 10% to each side) and every step has a
living cost. In earlier labs we solved this with value iteration, where T and
R were known. In this lab **we do not have T and R**, so the robot must learn
by acting in the environment.

## Folder structure

```
isolate/
├── CLAUDE.md                          # Main agent (orchestrator): project summary, which
│                                      # specialist gets which task, delegation rules
├── .claude/
│   └── agents/                        # Specialist sub-agents (YAML frontmatter + instructions)
│       ├── environment-specialist.md  # MDPEnvironment, default_world, percept(), execute_action()
│       ├── agent-specialist.md        # Agent programs (percept -> action); never sees T or R
│       ├── mdp-specialist.md          # value_iteration, TRANSITIONS, get_reward (model-based baseline)
│       └── code-review-specialist.md  # Read-only reviewer; sees only the changed code
└── README.md                          # This file
```

The notebooks (`markov.ipynb`, `vacuum_world.ipynb`, `agents.ipynb`) are in the
repository root and are shared with the Strategy 1 (`write/`) setup.

## How the files work together

1. You give Claude Code a task, for example "change the living cost and show the new policy."
2. Claude reads `CLAUDE.md` and learns it is the orchestrator and which specialists exist.
3. It delegates each part with a short, focused prompt. It does not pass the chat history.
4. Each specialist (`.claude/agents/*.md`) works only with its own context and
   the tools in its `tools:` list.
5. Each specialist returns a short summary. Only that summary goes back to the main agent.

| Specialist               | Knows about                                         | Can edit                 |
|--------------------------|-----------------------------------------------------|--------------------------|
| `environment-specialist` | grid internals, slip, rewards, living cost          | `MDPEnvironment`, `default_world` |
| `agent-specialist`       | only `percept()`, `execute_action()`, `performance` | agent programs           |
| `mdp-specialist`         | `TRANSITIONS`, `get_reward`, value iteration        | markov.ipynb helpers     |
| `code-review-specialist` | only the changed code                               | nothing (read-only)      |

**Why this split:** the `agent-specialist` is kept away from T and R in the same
way the robot is. Only the environment and MDP specialists see the transition
and reward details.

## Using it
Claude Code loads `CLAUDE.md` and `.claude/agents/` from the folder it is started
in, so start it inside `isolate/` and give it access to the notebooks one level up:

```bash
cd isolate
claude --add-dir ..
```

Then run `/agents` to see the four specialists and give the main agent a task.

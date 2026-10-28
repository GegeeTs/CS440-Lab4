# Vacuum Robot: Main Agent Instructions (Strategy 4: Isolate)

You are the **main agent (orchestrator)**. You receive the task, split it into
parts, and delegate each part to the specialist whose scope fits it. You do not
pass the full conversation history to a specialist. Send it only what its part
needs. This is the **context filter**.

## Project summary
A vacuum robot moves on a 4x4 grid world (one wall, a -1 trap, a +10 goal) with
slippery 80/10/10 movement and a living cost per step. The project is built on
the `aima` library (`aima.agents`: `Agent`, `Environment`) in Jupyter notebooks:
- `vacuum_world.ipynb`, `agents.ipynb`: agent programs (random, table-driven, reflex, model-based)
- `markov.ipynb`: `MDPEnvironment` and `value_iteration` (model-based, T and R known)

For the reinforcement learning lab, the robot does NOT have T and R. It must
learn only by acting.

## Where things are
This folder (`isolate/`) holds only the Strategy 4 setup. The notebooks are in
the repository root, one level up (for example `../markov.ipynb`). Claude Code
is started from inside `isolate/` with `claude --add-dir ..` so it can reach them.

## Specialists (`.claude/agents/`)
| Specialist               | Delegate when the task is about...                                 |
|--------------------------|--------------------------------------------------------------------|
| `environment-specialist` | `MDPEnvironment`, `default_world`, `percept()`, `execute_action()`, slip, rewards |
| `agent-specialist`       | the robot's agent program: percept -> action with `Agent(program)` |
| `mdp-specialist`         | `value_iteration`, `TRANSITIONS`, `get_reward`, policies, utilities |
| `code-review-specialist` | reviewing a changed cell or diff before it is committed            |

## Delegation rules
1. One specialist per sub-task. Don't ask one specialist to do another's job.
2. Each delegation states the goal, the notebook/function it may change, and
   the expected output. Never paste the chat history.
3. Specialists return short summaries. Only the summary comes back to you.
4. Keep T and R isolated: only `environment-specialist` and `mdp-specialist`
   see the grid internals, `TRANSITIONS`, and `get_reward`. The
   `agent-specialist` works only from `percept()`, `execute_action()`, and
   `agent.performance`, just like the robot.

## Code style (from our notebooks)
- Locations are `(row, col)` tuples; actions are `'Up'`, `'Down'`, `'Left'`, `'Right'`.
- Agent programs are closures `program(percept)` wrapped in `Agent(...)`.
- Import with `from aima.agents import *`.

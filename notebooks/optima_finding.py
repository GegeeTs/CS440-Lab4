# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# %run bootstrap.ipynb
from aima.agents import *
import math
import random


# %%
def HillClimbingAgent():

    def program(percept):
        location, status, surroundings = percept
        if status == 'Start':
            status = float('-inf')
        best_move = 'NoOp'
        best_move_value = status
        for move, value in surroundings.items():
            if value == 'Start':
                value = float('-inf')
            if value is not None and value > best_move_value:
                best_move_value = value
                best_move = move
        return best_move

    return program


# %%
def SimulatedAnnealingAgent(
    initial_temperature = 10.0,
    cooling_rate = 0.98,
    minimum_temperature = 0.01,
    max_steps = 1000,
    seed = 42
):
    rng = random.Random(seed)
    temperature = initial_temperature
    steps = 0
    
    def program(percept):
        nonlocal temperature, steps

        _, current_value, neighbors = percept
        choices = [
            (action, value)
            for action, value in neighbors.items()
            if value is not None
        ]

        if (temperature <= minimum_temperature or steps >= max_steps or not choices):
            program.done = True
            program.last_step = None
            return "NoOp"

        action, next_value = rng.choice(choices)
        delta = next_value - current_value

        probability = (1.0 if delta >= 0 else math.exp(delta / temperature))
        accepted = rng.random() < probability

        program.last_step = {
            "temperature": temperature,
            "proposal": action,
            "candidate_value": next_value,
            "probability": probability,
            "accepted": accepted
        }

        temperature *= cooling_rate
        steps += 1

        return action if accepted else "NoOp"

    program.done = False
    return program


# %% [markdown]
# We use the dirt level as our objective function because we want to find the dirtiest spot. The vacuum always accepts moves to cells with the same or more dirt. It can also accept moves to less dirty cells so it has a chance to escape a local maximum.
#
# We chose a starting temperature of 10 because the dirt levels range from 0 to 10. After each attempt, we multiply the temperature by 0.98, lowering it by 2%. This gives the vacuum time to explore at first, then makes it less likely to accept worse moves as it cools. The search stops when the temperature falls to 0.01 or lower, or after 1,000 attempts.

# %%
class NumericEnvironment(Environment):
    def __init__(self, env):
        super().__init__()
        self.status = env

    def thing_classes(self):
        """Return the Thing/Agent classes that may populate this vacuum world."""
        return [Wall, Dirt, HillClimbingAgent, SimulatedAnnealingAgent]

    def percept(self, agent):
        """Returns the agent's location, and the location status, as well as
        the status of the places the agent can move to on the next move."""

        surroundings = {'Up': None,
                        'Down': None,
                        'Left': None,
                        'Right': None}
        
        if (x:= agent.location[1] + 1) < len(self.status[0]):
            surroundings['Up'] = self.status[agent.location[0]][x]
        if (x:= agent.location[1] - 1) >= 0:
            surroundings['Down'] = self.status[agent.location[0]][x]
        if (x:= agent.location[0] - 1) >= 0:
            surroundings['Left'] = self.status[x][agent.location[1]]
        if (x:= agent.location[0] + 1) < len(self.status):
            surroundings['Right'] = self.status[x][agent.location[1]]

        return agent.location, self.status[agent.location[0]][agent.location[1]], surroundings

    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned; -1 for each move."""
        if action == 'Right':
            newX = agent.location[0] + 1
            if newX >= len(self.status[0]):
                raise Exception('Cannot move out of bounds')
            agent.location = (newX, agent.location[1])
            agent.performance -= 1
        elif action == 'Left':
            newX = agent.location[0] - 1
            if newX < 0:
                raise Exception('Cannot move out of bounds')
            agent.location = (newX, agent.location[1])
            agent.performance -= 1
        elif action == 'Up':
            newY = agent.location[1] + 1
            if newY >= len(self.status):
                raise Exception('Cannot move out of bounds')
            agent.location = (agent.location[0], newY)
            agent.performance -= 1
        elif action == 'Down':
            newY = agent.location[1] - 1
            if newY < 0:
                raise Exception('Cannot move out of bounds')
            agent.location = (agent.location[0], newY)
            agent.performance -= 1
        elif action == 'Suck':
            x, y = agent.location
            if self.status[x][y] == 'Dirty':
                agent.performance += 10
            self.status[x][y] = 'Clean'
        elif action == 'NoOp':
            agent.performance -= 1

    def default_location(self, thing):
        """Agents start in either location at random."""
        return (0, 3)

    def __str__(self):
        return str(self.status)



# %%
class AnnealingEnvironment(NumericEnvironment):
    directions = {
        "Up": (-1, 0),
        "Down": (1, 0),
        "Left": (0, -1),
        "Right": (0, 1)
    }

    def percept(self, agent):
        row, col = agent.location
        neighbors = {}

        for action, (dr, dc) in self.directions.items():
            nr, nc = row + dr, col + dc

            if (0 <= nr < len(self.status) and 0 <= nc < len(self.status[nr])):
                value = self.status[nr][nc]
                neighbors[action] = 0 if value == "Start" else value
            else:
                neighbors[action] = None

        value = self.status[row][col]
        current_value = 0 if value == "Start" else value

        return agent.location, current_value, neighbors

    def execute_action(self, agent, action):
        if action == "NoOp":
            return

        dr, dc = self.directions[action]
        row, col = agent.location
        nr, nc = row + dr, col + dc

        if not (0 <= nr < len(self.status) and 0 <= nc < len(self.status[nr])):
            raise ValueError("Cannot move out of bounds")

        agent.location = (nr, nc)
        agent.performance -= 1


annealing_board = [
    [0, 3, 2, "Start"],
    [3, 6, 0, 0],
    [5, 0, 6, 8],
    [4, 9, 0, 10]
]

annealing_environment = AnnealingEnvironment(
    [row[:] for row in annealing_board]
)

annealing_program = SimulatedAnnealingAgent(
    initial_temperature=10.0,
    cooling_rate=0.98,
    minimum_temperature=0.01,
    max_steps=1000,
    seed=42
)

annealer = Agent(annealing_program)
annealing_environment.add_thing(annealer)

path = [annealer.location]
best_location = annealer.location
best_value = annealing_environment.percept(annealer)[1]

while not annealing_program.done:
    annealing_environment.step()

    if annealing_program.done:
        break

    location, value, _ = annealing_environment.percept(annealer)
    path.append(location)

    if value > best_value:
        best_location = location
        best_value = value

print("Path:", " -> ".join(str(position) for position in path))
print(f"Dirtiest spot found: {best_location}, dirt={best_value}")

# %%
hill_climbing_board = [[0, 3, 2, 'Start'],
                       [0, 0, 0, 0],
                       [0, 4, 6, 8],
                       [7, 9, 0, 10]]
hill_climbing_environment = NumericEnvironment(hill_climbing_board)

hill_climber = Agent(HillClimbingAgent())

hill_climbing_environment.add_thing(hill_climber)
print(f'Hill Climbing Agent located at {hill_climber.location}')

# %%
path = [hill_climber.location]
status = hill_climbing_environment.status
r, c = hill_climber.location
# %%
for step in range(1,17):
    start = hill_climber.location
    hill_climbing_environment.step()
    if hill_climber.location == start:
        break
    path.append(hill_climber.location)
    r, c = hill_climber.location
    print(f"{step:<6}{str(hill_climber.location):<10}{status[r][c]}")
final_hill = hill_climber.location
print("State of the Environment: {}.".format(hill_climbing_environment.status))
print(f'Hill Climbing Agent located at {hill_climber.location}')
print("\nPath of hill climber:", " -> ".join(str(g) for g in path))
print(f"Stopped at {final_hill} with a level of {status[final_hill[0]][final_hill[1]]}")


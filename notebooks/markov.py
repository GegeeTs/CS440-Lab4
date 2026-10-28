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
import random

# %%
default_world = [[0, 0,   0, 'start'],
                 [0, 'X', 0, 0],
                 [0, 0,   0, 0],
                 [0, -1,  0, 10]]

class MDPEnvironment(Environment):
    def __init__(self, env=default_world, living_cost=1):
            super().__init__()
            self.status = env
            self.cost = living_cost

    def percept(self, agent):
            """Returns the agent's location, and the location status."""
            return agent.location, self.status[agent.location[0]][agent.location[1]]

    def execute_action(self, agent, action):
        if self.status[agent.location[0]][agent.location[1]] == -1:
            return # agent is "dead" so no cost is incurred 
        agent.performance -= self.cost

        if action == 'Right':
            self._attempt(agent, self._right, self._up, self._down)   
        elif action == 'Up':
            self._attempt(agent, self._up, self._right, self._left)
        elif action == 'Down':
            self._attempt(agent, self._down, self._left, self._right)
        elif action == 'Left':
            self._attempt(agent, self._left, self._up, self._down)

        self._check_reward(agent)

    def _attempt(self, agent, intended_action, accidental_action1, accidental_action2):
        slip = random.random()
        tup = slip < 0.8, slip >= 0.9

        match tup:
            case True, _:
                intended_action(agent)
            case _, False:
                accidental_action1(agent)
            case _, True:
                accidental_action2(agent)

    def _check_reward(self, agent):
        if self.status[agent.location[0]][agent.location[1]] == 10:
            agent.performance += 10 # agent gets the reward

    """ Movements are named so that they correspond to the actual direction.
    For example, an agent at list indices (0, 1)
    could go down to make the new list indices (1, 1),
    or it could go left to make the new list indices (0, 0)"""

    def _down(self, agent):
        newX = agent.location[0] + 1
        Y = agent.location[1]
        if not (newX >= len(self.status[0]) or self.status[newX][Y] == 'X'):
            agent.location = newX, Y

    def _up(self, agent):
        newX = agent.location[0] - 1
        Y = agent.location[1]
        if not (newX < 0 or self.status[newX][Y] == 'X'):
            agent.location = newX, Y

    def _right(self, agent):
        X = agent.location[0]
        newY = agent.location[1] + 1
        if not (newY >= len(self.status) or self.status[X][newY] == 'X'):
            agent.location = X, newY

    def _left(self, agent):
        X = agent.location[0]
        newY = agent.location[1] - 1
        if not (newY < 0 or self.status[X][newY] == 'X'):
            agent.location = X, newY

    def default_location(self, thing):
        for i, list in enumerate(self.status):
            for j, element in enumerate(list):
                if element == 'start':
                    return (i, j)

    def __str__(self):
        return str(self.status)



# %%
ACTIONS = ['Up', 'Down', 'Left', 'Right']

DIRECTIONS = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}

TRANSITIONS = {
    'Up': [('Up', 0.8), ('Left', 0.1), ('Right', 0.1)],
    'Down': [('Down', 0.8), ('Left', 0.1), ('Right', 0.1)],
    'Left': [('Left', 0.8), ('Up', 0.1), ('Down', 0.1)],
    'Right': [('Right', 0.8), ('Up', 0.1), ('Down', 0.1)]
}


def move(state, action, world):
    row, col = state
    dr, dc = DIRECTIONS[action]

    new_row = row + dr
    new_col = col + dc

    if not (0 <= new_row < len(world)):
        return state

    if not (0 <= new_col < len(world[0])):
        return state

    if world[new_row][new_col] == 'X':
        return state

    return (new_row, new_col)


def get_reward(state, world):
    row, col = state

    if world[row][col] == 10:
        return 10

    if world[row][col] == -1:
        return -1

    return 0


def is_terminal(state, world):
    row, col = state
    return world[row][col] in (10, -1)

# Calculates the expected reward of an action using the 80/10/10 probabilities
def expected_utility(state, action, utilities, world, living_cost, gamma):

    total = 0

    for direction, probability in TRANSITIONS[action]:
        next_state = move(state, direction, world)
        reward = get_reward(next_state, world)
        total += probability * (reward + gamma * utilities[next_state])

    return -living_cost + total


def value_iteration(world, living_cost=1, gamma=0.95, tolerance=0.0001):
    states = []

    for r in range(len(world)):
        for c in range(len(world[0])):
            if world[r][c] != 'X':
                states.append((r, c))

    utilities = {state: 0.0 for state in states}

    while True:
        new_utilities = utilities.copy()
        delta = 0

        for state in states:
            if is_terminal(state, world):
                continue

            best_value = max(expected_utility(state, action, utilities, world, living_cost, gamma) for action in ACTIONS)
            new_utilities[state] = best_value
            delta = max(delta, abs(best_value - utilities[state]))

        utilities = new_utilities

        if delta < tolerance:
            break

    # Find the best action at each position
    policy = {}

    for state in states:
        if is_terminal(state, world):
            continue

        policy[state] = max(ACTIONS, key=lambda action: expected_utility(state, action, utilities, world, living_cost, gamma))

    return utilities, policy



# %%
def run_robot(policy, living_cost=1, max_steps=100):
    env = MDPEnvironment(living_cost=living_cost)
    robot = Agent(lambda percept: None)
    robot.location = env.default_location(robot)

    path = [robot.location]

    for step in range(max_steps):
        current = robot.location
        action = policy[current]

        env.execute_action(robot, action)
        path.append(robot.location)

        print(f"Step {step + 1}: {current} -> {action} -> {robot.location}")

        row, col = robot.location
        if env.status[row][col] in (10, -1):
            if env.status[row][col] == -1:
                robot.performance -= 1
            break

    print("Path:", path)
    print("Total reward:", robot.performance)

    return path



# %%
living_cost = 1

utilities, policy = value_iteration(default_world, living_cost=living_cost)

print()

path = run_robot(policy, living_cost=living_cost)


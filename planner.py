import sys
import heapq
from collections import deque

def ucs(world_grid, start, goals):
    """Uniform Cost Search algorithm-- finds optimal (minimum cost) plan"""

    frontier = []  # unexplored nodes (LIFO)-- quadruples of (cost, current state, goals remaining, path)
    heapq.heappush(frontier, (0, start, goals, []))  # add start state to frontier priority queue
    visited = set() # explored nodes-- tuples of (state, goals remaining)

    # keep track of these deliverables
    nodes_generated = 0
    nodes_expanded = 0

    while frontier:
        cost, current_state, current_goals, path = heapq.heappop(frontier)

        # check if current node has been visited
        if not ((current_state, current_goals) in visited):
            visited.add((current_state, current_goals))  # mark current node as visited
            nodes_expanded += 1

        # grid cleaned-- no more goal states
        if not current_goals:
            # print deliverables
            for action in path:
                print(action)
            print(f"{nodes_generated} nodes generated")
            print(f"{nodes_expanded} nodes expanded")
            return

        # grid not clean-- expand current state
        # traverse valid actions from current state
        for new_state, new_goals, action in valid_actions(current_state, current_goals, world_grid):
            if (new_state, new_goals) not in visited:  # successor not visited
                heapq.heappush(frontier, (cost + 1, new_state, new_goals, path + [action]))  # add node to unexplored
                nodes_generated += 1

    print("Failure to clean world grid")

def dfs(world_grid, start, goals):
    """Depth First Search algorithm-- avoids infinite loops or cycles"""

    frontier = deque() # unexplored nodes (FIFO)-- triples of (current state, goals remaining, path)
    visited = set() # explored nodes-- tuples of (state, goals remaining)

    # add start state to frontier stack-- start pos, goal states, path
    frontier.append((start, goals, []))

    # keep track of these deliverables
    nodes_generated = 0
    nodes_expanded = 0

    while frontier:
        current_state, current_goals, path = frontier.pop()

        # check if current node has been visited
        if not ((current_state, current_goals) in visited):
            visited.add((current_state, current_goals)) # mark current node as visited
            nodes_expanded += 1

        # grid cleaned-- no more goal states
        if not current_goals:
            # print deliverables
            for action in path:
                print(action)
            print(f"{nodes_generated} nodes generated")
            print(f"{nodes_expanded} nodes expanded")
            return

        # grid not clean-- expand current state
        # traverse valid actions from current state
        for new_state, new_goals, action in valid_actions(current_state, current_goals, world_grid):
            if (new_state, new_goals) not in visited:  # successor not visited
                frontier.append((new_state, new_goals, path + [action]))  # add node to unexplored
                nodes_generated += 1

    print("Failure to clean world grid")


def valid_actions(current_state, goals, world_grid):
    """Returns a set of actions (new_state, remaining_goals, action) the vacuum can perform in a given state"""

    # action directions
    directions = {
        'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1)
    }

    # define current state coordinates
    curr_r, curr_c = current_state
    # define dimensions
    grid_rows = len(world_grid)
    grid_cols = len(world_grid[0])
    actions = []

    # iterate through possible directions
    for direction, (dr, dc) in directions.items():
        new_r, new_c = dr + curr_r, dc + curr_c  # compute new state position
        if 0 <= new_r < grid_rows and 0 <= new_c < grid_cols:  # new state position is within grid
            if world_grid[new_r][new_c] != '#':  # new state position is an open cell
                actions.append(((new_r, new_c), goals.copy(), direction))  # append valid action

    # check if we can vacuum
    if (curr_r, curr_c) in goals:
        new_goals = goals - {(curr_r, curr_c)}
        actions.append(((curr_r, curr_c), new_goals, 'V'))

    return actions


if __name__=="__main__":
    if len(sys.argv) != 3:
        print("Usage: planner.py takes 2 arguments-- <algorithm> <world-file>")
        sys.exit(1)

    algorithm = sys.argv[1] # search algorithm to execute
    world_file = sys.argv[2] # world file to vacuum clean

    # check for valid search algorithm argument
    if algorithm not in ["uniform-cost", "depth-first"]:
        print("Error: algorithm must be 'uniform-cost' or 'depth-first'")
        sys.exit(1)

    # check for valid .txt world file
    if not world_file.endswith(".txt"):
        print("Error: world file must be a .txt file")
        sys.exit(1)

    # open world file
    try:
        with open(world_file, 'r') as input_file:

            # read world file into lines
            lines = [line.strip() for line in input_file.readlines()]

            # identifying details
            cols = int(lines[0])
            rows = int(lines[1])
            grid = [list(line) for line in lines[2:]] # 2D list

            # validate rows and columns
            if len(grid) != rows:
                print(f"Error: Grid contains {len(grid)}, expected {rows}")
                sys.exit(1)
            for i in range(len(grid)):
                if len(grid[i]) != cols:
                    print(f"Error: Row {i} has {len(grid[i])} columns, expected {cols}")
                    sys.exit(1)

            # locate:
            # starting state --initial position--(@)
            # goal state(s)--dirty cells--(*)
            start_state = None
            goal_states = set()
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == "@":
                        if start_state is None: # found start state
                            start_state = (r, c)
                        else:  # found a second start state-- invalid
                            print("Error: There can only be one '@' representing the start state, found more than one")
                            sys.exit(1)
                    elif grid[r][c] == "*":
                        goal_states.add((r, c))  # found a goal state

            if start_state is None:  # no start state found
                print("Error: No starting position '@' found in grid")
                sys.exit(1)

            # call specified search algorithm to compute vacuum plan
            if algorithm == "uniform-cost":
                ucs(grid, start_state, frozenset(goal_states))
            else:
                dfs(grid, start_state, frozenset(goal_states))


    except FileNotFoundError:
        print(f"Error: File '{world_file}' not found")
        sys.exit(1)
    except IOError:
        print(f"Error: Could not read file '{world_file}'")
        sys.exit(1)


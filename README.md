# Project 1: Vacuum Robot Planner

**Implemented search algorithms:**
- uniform cost search (UCS)
  - produces an optimal (minimum cost) plan 
- depth first search (DFS)
  - avoids infinite loops/ cycles

**Input: .txt file containing a grid world.**
- line 1 includes number of columns
- line 2 includes number of rows
- remaining lines contains grid

**Output: plan/ sequence of actions (N, S, E, W, V), number of nodes generated, number of nodes expanded**

**Program execution from command line: python3 planner.py <algorithm> <world-file>**
- algorithm specifies search algorithm
  - either: uniform-cost or depth-first
- world-file specifies the path to the .txt file

**Command line execution**
- making the world grid:
  `./make_vacuum_world.py <row> <column> <percentage of blocked cells> <dirty cells> > <txt file>`
- running vacuum plan
  `python3 planner.py <algorithm> <txt file>`


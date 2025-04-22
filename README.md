# Project 1: Vacuum Robot Planner

- implemented search algorithms
  - uniform cost search (UCS)
    - produces an optimal (minimum cost) plan 
  - depth first search (DFS)
    - avoids infinite loops/ cycles

Input: .txt file containing a grid world. 
- line 1 includes number of columns
- line 2 includes number of rows
- remaining lines contains grid

Output: plan/ sequence of actions (N, S, E, W, V), number of nodes generated, number of nodes expanded

Program execution from command line: python3 planner.py <algorithm> <world-file>
- algorithm specifies search algorithm
- world-file specifies the path to the .txt file


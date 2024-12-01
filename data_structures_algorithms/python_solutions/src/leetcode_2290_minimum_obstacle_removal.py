'''
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
'''

import math
from typing import List
import heapq

DIRECTIONS = [(-1,0),(0,-1),(1,0),(0,1),]

def solution(grid: List[List[int]]) -> int:
    '''
    Idea 1 ((m*n)**2): explore all possible paths from top left to bottom right and keep count of the number of obstacles in each, return the minimum
    
    Idea 2: 
    Each element in the matrix is a node in a graph.
    All edges leading into an empty cell have a weight of 0.
    All edges leading into a cell with an obstacle have a weight of 1.
    We need to find the shortest path from top left to bottom right.
    The graph is cyclic.
    
    Use an algorithm designed for finding the shortest path between two nodes in a directed, cyclic graph
    
    Solution uses dijsktras
    
    Sub problem: how to keep track of the "next node" candidates and choose the one with the lowest distance     
    Sub idea 1 O(m * n): scan the entire distance matrix...
    Sub idea 2 O(n): maintain a set of possible next nodes, add to the set when updating neighbour distances, remove when selecting next node
    Sub idea 3 O(log n): maintain a priority queue of next nodes similar to above but with O(log n) fetch rather than O(n)s
    I did each of them and settled on sub idea 3.
    
    I decided to optimise on memory after getting a working dijsktras with a heap for next_nodes.
    I got past the runtime exceptions for a few of the biggest testcases on leetcode.
    
    The below code beats 14.86% in runtime and 80.89% in memory. 
    
    There's wasted compute spent putting duplicate nodes in next_nodes and then cycling past them by checking to see if they are visited
    I could optimise there but already went over timebox on this one.
    
    Looking at leetcode, BFS is the fastest solution...
    '''
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    next_nodes_heap = []
    
    def add_next_nodes(node_m: int, node_n: int, distance: int) -> None:
        for dir_n, dir_m in DIRECTIONS:
            neighbour_n = node_n + dir_n
            neighbour_m = node_m + dir_m
            in_bounds = neighbour_n >= 0 and neighbour_n < len(grid[0]) and neighbour_m >= 0 and neighbour_m < len(grid)
            if in_bounds and not visited[neighbour_m][neighbour_n]:
                weight = grid[neighbour_m][neighbour_n]
                new_distance = distance + weight
                heapq.heappush(next_nodes_heap, (new_distance, (neighbour_m, neighbour_n)))
                    
    def pick_next_node() -> tuple:
        distance, (m, n) = heapq.heappop(next_nodes_heap)
        while visited[m][n]:
            distance, (m, n) = heapq.heappop(next_nodes_heap)
        return distance, (m,n)
            
    distance = 0
    add_next_nodes(0, 0, distance=0)
    visited[0][0] = True

    while not visited[-1][-1]:
        distance, (next_node_m, next_node_n) = pick_next_node()
        add_next_nodes(next_node_m, next_node_n, distance)
        visited[next_node_m][next_node_n] = True
        if next_node_m == len(grid) - 1 and next_node_n == len(grid[0]) - 1:
            return distance
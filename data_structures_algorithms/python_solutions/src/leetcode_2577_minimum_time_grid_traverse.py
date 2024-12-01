'''
You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] 
represents the minimum time required to be able to visit the cell (row, col), which means you 
can visit the cell (row, col) only when the time you visit it is greater than or equal to 
grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to 
any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 
1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. 
If you cannot visit the bottom-right cell, then return -1.
'''

from typing import List
import heapq

def solution(grid: List[List[int]]) -> int:
    '''
    Idea 1:
    Straight away I'm seeing a BFS solution here.
    There is a tree of moves that can be made from the root. 
    Each level represents 1 more "time" value.
    Use BFS to find a path to the end and return the value of the level.
    
    Idea 1, simple naive BFS with a queue, was too slow. 
    We need a way to optimise it.
    Dijkstras seems to be mentioned on leetcode.
    Rather than rewrite to Dijkstra's, to save myself time, I'm going to try optimise.
    Instead of using a queue and looking at all possible moves,
    use a priority queue based on "time" to pick the next move.
    To move from node x to node y, we can either do that immediately
    if time_y <= time_x or we have to move 
    (time_y-time_x) + (time_y-time_x) % 2 times
    e.g. if the diff is 3 we move 4, if the diff is 4 we move 4.
    this accounts for going backwards and forwards to reach the time needed to traverse there
    
    still not fast enough. need to come back and switch to proper Dijkstra's I think
    '''    
    if grid[0][0] > 0:
        return -1
    
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    
    len_y, len_x = len(grid), len(grid[0])
    
    visited = [[False for _ in range(len_x)] for _ in range(len_y)]
    
    next_directions = []
    
    def in_bounds(x: int, y: int) -> bool:
        return x >= 0 and x < len_x and y >= 0 and y < len_y
    
    def reached_end(x: int, y: int) -> bool:
        return x == len_x - 1 and y == len_y - 1
    
    def add_next_directions(x: int, y: int, time: int) -> None:
        '''
        Return True if we have reached the end
        Otherwise add the next directions to move to into a queue for BFS traversal
        '''
        for dir_x, dir_y in directions:
            next_x = x + dir_x
            next_y = y + dir_y
            if in_bounds(next_x, next_y) and not visited[next_y][next_x]:
                next_grid_time_needed = grid[next_y][next_x]
                if next_grid_time_needed <= time + 1:
                    heapq.heappush(next_directions, (time+1, (next_x, next_y)))
                elif time > 0:  # Move backwards and forwards to reach the next node - only possible if not on [0][0]
                    extra_time_needed = next_grid_time_needed - time
                    min_time_to_node = extra_time_needed + (extra_time_needed % 2)
                    heapq.heappush(next_directions, (time+min_time_to_node, (next_x, next_y)))
   
    x = 0
    y = 0
    time = 0
    heapq.heappush(next_directions, (time, (x, y)))
    while next_directions:
        time, node = heapq.heappop(next_directions)
        visited[node[1]][node[0]] = True
        if reached_end(node[0], node[1]):
            return time+1
        add_next_directions(node[0], node[1], time)
    
    return -1

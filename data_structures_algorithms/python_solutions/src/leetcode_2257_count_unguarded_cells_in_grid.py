'''
https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
You are given two integers m and n representing a 0-indexed m x n grid. 
You are also given two 2D integer arrays guards and walls where 
guards[i] = [rowi, coli] and walls[j] = [rowj, colj] 
represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions 
(north, east, south, or west) starting from their position unless 
obstructed by a wall or another guard. A cell is guarded if there is 
at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.
'''
from typing import List

EMPTY = 0
NOT_EMPTY = 1

def solution(m: int, n: int, guards: List[List[int]], walls: List[List[int]]): 
    '''
    Will treat m and n as constants when I simplify complexities below
    
    Idea 1:
    O(g)
    Loop through all guards
    O(m + n) * O(g + w) 
    Check in each cardinal direction until you hit either the end of the matrix or a wall or a guard. need to search in guards and walls list each time
    O(1)
    Add each guarded, empty square to a set (hashtable) so to avoid duplicates
    O(1)
    Get total squares mxn and return total - len(guards) - len(walls) - len(guarded_square_set)
    Complexity = O(g(mg + ng + mw + nw)) = g**2 + w
    
    Idea 2:
    O(1)
    Create a matrix
    O(g)
    Loop through guards and add to matrix
    O(w)
    Loop through walls and add to matrix
    O(gm + gn)
    Then do as idea 1
    Complexity = g + w
    
    Let's try idea 2.
    
    Idea 3:
    Don't use a guarded_squares set, just set the square in the matrix to something other than empty then return a count of empty squares in the matrix
    Uses less space, a tiny bit faster
    
    Below is idea 2 implemented. Beats 63% in runtime and 57% in memory on leetcode.
    '''
    matrix = [[EMPTY for _ in range(n)] for _ in range(m)]
    
    for guard_m, guard_n in guards:
        matrix[guard_m][guard_n] = NOT_EMPTY
        
    for wall_m, wall_n in walls:
        matrix[wall_m][wall_n] = NOT_EMPTY
        
    guarded_squares = set()

    for g_m, g_n in guards:
        # check up
        index_m = g_m - 1
        while index_m >= 0 and matrix[index_m][g_n] == EMPTY:
            guarded_squares.add(tuple([index_m, g_n]))
            index_m -= 1
        # check right
        index_n = g_n + 1
        while index_n < n and matrix[g_m][index_n] == EMPTY:
            guarded_squares.add(tuple([g_m, index_n]))
            index_n += 1
        # check down
        index_m = g_m + 1
        while index_m < m and matrix[index_m][g_n] == EMPTY:
            guarded_squares.add(tuple([index_m, g_n]))
            index_m += 1
        # check left
        index_n = g_n - 1
        while index_n >= 0 and matrix[g_m][index_n] == EMPTY:
            guarded_squares.add(tuple([g_m, index_n]))
            index_n -= 1      
    
    total_squares = m * n
    return total_squares - len(guards) - len(walls) - len(guarded_squares)
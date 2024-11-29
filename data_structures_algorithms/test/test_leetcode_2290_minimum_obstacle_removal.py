import pytest
from typing import List
from data_structures_algorithms.src.leetcode_2290_minimum_obstacle_removal import solution


test_data = [
    ([[0,1,1],[1,1,0],[1,1,0]], 2),
    ([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], 0),
    ([[0,1,1,1,0]], 3),
    ([[0,0,1,1],[1,1,1,1],[0,1,1,1],[1,1,0,1],[1,1,1,1],[1,0,1,0],[1,1,1,1],[1,1,1,1],[1,1,1,0],[0,1,0,0]], 7),
]


@pytest.mark.parametrize("grid, expected", test_data)
def test_solution(grid: List[List[int]], expected: int):
    assert solution(grid) == expected
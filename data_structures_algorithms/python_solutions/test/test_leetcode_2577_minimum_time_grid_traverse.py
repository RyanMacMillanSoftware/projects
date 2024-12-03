import pytest
from typing import List
from data_structures_algorithms.python_solutions.src.leetcode_2577_minimum_time_grid_traverse import solution


test_data = [
    ([[0,1,3,2],[5,1,2,5],[4,3,8,6]], 7),
    ([[0,2,4],[3,2,1],[1,0,4]], -1),
]

@pytest.mark.parametrize("grid, expected", test_data)
def test_solution(grid: List[List[int]], expected: int):
    assert solution(grid) == expected
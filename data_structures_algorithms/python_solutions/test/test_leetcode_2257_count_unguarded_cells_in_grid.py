from typing import List
import pytest

from data_structures_algorithms.python_solutions.src.leetcode_2257_count_unguarded_cells_in_grid import solution

test_data = [
    (4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]], 7),
    (3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]], 4)
]


@pytest.mark.parametrize("m, n, guards, walls, expected", test_data)
def test_solution(m: int, n: int, guards: List[List[int]], walls: List[List[int]], expected: int):
    assert solution(m, n, guards, walls) == expected
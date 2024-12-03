from typing import List
import pytest

from data_structures_algorithms.python_solutions.src.leetcode_2109_medium_adding_spaces_to_string import add_spaces


test_data = [
    ("LeetcodeHelpsMeLearn", [8,13,15], "Leetcode Helps Me Learn"),
    ("icodeinpython", [1,5,7,9], "i code in py thon"),
    ("spacing", [0,1,2,3,4,5,6],  " s p a c i n g"),
]


@pytest.mark.parametrize("s, spaces, expected", test_data)
def test_solution(s: str, spaces: List[int], expected: str):
    assert add_spaces(s, spaces) == expected
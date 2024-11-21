import pytest

from data_structures_algorithms.src.leetcode_2561_take_k_of_each_character import solution

test_data = [
    ("aabaaaacaabc", 2, 8),
    ("a", 1, -1),
]

@pytest.mark.parametrize("s, k, expected", test_data)
def test_solution(s, k, expected):
    assert solution(s, k) == expected
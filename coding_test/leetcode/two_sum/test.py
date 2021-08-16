import pytest

from .solution import Solution


@pytest.fixture(scope="module")
def solution():
    s = Solution()
    return s.twoSum


def test_solution(solution):
    assert solution([2, 7, 11, 15], 9) == [0, 1]
    assert solution([3, 2, 3], 6) == [0, 2]
    assert solution([3, 3], 6) == [0, 1]
    assert solution([1, 2, 1], 2) == [0, 2]
    assert solution([1, 3, 1, 2, 1], 5) == [1, 3]

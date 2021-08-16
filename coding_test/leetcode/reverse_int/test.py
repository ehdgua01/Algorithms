import pytest

from .solution import Solution


@pytest.fixture(scope="module")
def solution():
    s = Solution()
    return s.reverse


def test_solution(solution):
    assert solution(123) == 321
    assert solution(-123) == -321
    assert solution(120) == 21
    assert solution(0) == 0
    assert solution(-9463847412) == 0
    assert solution(8463847412) == 0

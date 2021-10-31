import pytest

from .solution import Solution


@pytest.fixture
def solution():
    return Solution().isPalindrome


@pytest.mark.parametrize(
    "value,expected",
    ((121, True), (-121, False), (10, False), (-101, False), (12321, True), (11, True)),
)
def test_solution(solution, value: int, expected: bool):
    assert solution(value) is expected

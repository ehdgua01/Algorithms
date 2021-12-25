from .solution import Solution


def test_solution():
    calculate = Solution().calculate
    assert calculate("3+2*2") == 7
    assert calculate(" 3/2 ") == 1
    assert calculate(" 3+5 / 2 ") == 5

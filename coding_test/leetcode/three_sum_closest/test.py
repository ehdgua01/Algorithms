from .solution import Solution


def test_solution():
    three_sum_closest = Solution().threeSumClosest
    assert three_sum_closest([-1, 2, 1, -4], 1) == 2
    assert three_sum_closest([0, 0, 0], 1) == 0
    assert three_sum_closest([1, 1, 1, 0], 100) == 3

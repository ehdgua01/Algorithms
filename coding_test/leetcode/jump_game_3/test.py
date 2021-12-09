from .solution import Solution


def test_solution():
    can_reach = Solution().canReach
    assert can_reach([4, 2, 3, 0, 3, 1, 2], 5)
    assert can_reach([4, 2, 3, 0, 3, 1, 2], 0)
    assert not can_reach([3, 0, 2, 1, 2], 2)

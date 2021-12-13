from .solution import Solution


def test_solution():
    can_partition = Solution().canPartition
    assert can_partition([1, 5, 11, 5])
    assert not can_partition([1, 2, 3, 5])
    assert can_partition([2, 2, 1, 1])
    assert not can_partition([2])

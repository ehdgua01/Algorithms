from .solution import Solution


def test_solution():
    solution = Solution()
    assert solution.maxArea([1, 1]) == 1
    assert solution.maxArea([4, 3, 2, 1, 4]) == 16
    assert solution.maxArea([1, 2, 1]) == 2
    assert solution.maxArea([7, 8, 9, 3, 5]) == 20
    assert solution.maxArea([7, 8, 9, 3, 9, 5]) == 28

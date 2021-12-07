from .solution import Solution


def test_solution():
    solution = Solution()
    assert solution.minCostToMoveChips([1, 2, 3]) == 1
    assert solution.minCostToMoveChips([2, 2, 2, 3, 3]) == 2
    assert solution.minCostToMoveChips([1, 1_000_000_000]) == 1

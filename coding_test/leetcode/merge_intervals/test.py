from .solution import Solution


def test_solution():
    merge = Solution().merge
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [1, 4]]) == [[1, 4]]
    assert merge([[1, 4], [2, 3]]) == [[1, 4]]

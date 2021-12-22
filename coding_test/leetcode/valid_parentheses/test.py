from .solution import Solution


def test_solution():
    is_valid = Solution().isValid
    assert is_valid("()")
    assert is_valid("()[]{}")
    assert not is_valid("(]")

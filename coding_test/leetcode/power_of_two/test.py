from .solution import Solution


def test_solution():
    is_power_of_two = Solution().isPowerOfTwo
    assert is_power_of_two(1)
    assert is_power_of_two(16)
    assert not is_power_of_two(3)

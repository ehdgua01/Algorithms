from .solution import Solution


def test_solution():
    max_power = Solution().maxPower
    assert max_power("leetcode") == 2
    assert max_power("abbcccddddeeeeedcba") == 5
    assert max_power("triplepillooooow") == 5
    assert max_power("hooraaaaaaaaaaay") == 11
    assert max_power("tourist") == 1
    assert max_power("cc") == 2

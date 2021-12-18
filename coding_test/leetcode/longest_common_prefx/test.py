from .solution import Solution


def test_solution():
    longest_common_prefix = Solution().longestCommonPrefix
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix([""]) == ""
    assert longest_common_prefix(["a"]) == "a"
    assert longest_common_prefix(["ab", "b"]) == ""

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict, t_dict = Counter(s), Counter(t)
        for key, count in t_dict.items():
            if key not in s_dict or count != s_dict[key]:
                return key


def test_solution():
    find_the_difference = Solution().findTheDifference
    assert find_the_difference("abcd", "abcde") == "e"
    assert find_the_difference("", "y") == "y"

import unittest

from .solution import Solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        __solution = Solution()
        self.assertEqual(__solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(__solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(__solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(__solution.lengthOfLongestSubstring(" "), 1)

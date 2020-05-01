import unittest

from .solution import Solution


class TestCse(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution().longestPalindrome

    def test_case_1(self) -> None:
        self.assertEqual(self.solution("babad"), "aba")
        self.assertEqual(self.solution("cbbd"), "bb")
        self.assertEqual(self.solution("abacd"), "aba")
        self.assertEqual(self.solution("bbcad"), "bb")

    def test_case_2(self) -> None:
        self.assertEqual(self.solution(""), "")
        self.assertEqual(self.solution("abba"), "abba")

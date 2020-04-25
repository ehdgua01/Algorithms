import unittest

from .solution import Solution


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_case_1(self) -> None:
        self.assertEqual(self.solution.myAtoi("42"), 42)
        self.assertEqual(self.solution.myAtoi("   -42"), -42)
        self.assertEqual(self.solution.myAtoi("-5-"), -5)

    def test_case_2(self) -> None:
        self.assertEqual(self.solution.myAtoi("4193 with words"), 4193)
        self.assertEqual(self.solution.myAtoi("words and 987"), 0)

    def test_case_3(self) -> None:
        self.assertEqual(self.solution.myAtoi("-91283472332"), -2147483648)

    def test_case_4(self) -> None:
        self.assertEqual(self.solution.myAtoi("+"), 0)
        self.assertEqual(self.solution.myAtoi("+-1"), 0)

import unittest

from .solution import Solution


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution().convert

    def test_case_1(self) -> None:
        string = "PAYPALISHIRING"
        self.assertEqual(self.solution(string, 3), "PAHNAPLSIIGYIR")
        self.assertEqual(self.solution(string, 4), "PINALSIGYAHRPI")

import unittest

from .solution import Solution


class TestCse(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution().maximum_69_Number

    def test_case_1(self) -> None:
        self.assertEqual(self.solution(6999), "9999")
        self.assertEqual(self.solution(96699), "99699")
        self.assertEqual(self.solution(9999), "9999")
        self.assertEqual(self.solution(6666), "9666")

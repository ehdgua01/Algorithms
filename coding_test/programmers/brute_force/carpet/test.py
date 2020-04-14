import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(solution(10, 2), [4, 3])
        self.assertEqual(solution(8, 1), [3, 3])
        self.assertEqual(solution(24, 24), [8, 6])
        self.assertEqual(solution(18, 6), [8, 3])
        self.assertEqual(solution(18, 12), [6, 5])

import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(529), 4)
        self.assertEqual(solution(20), 1)
        self.assertEqual(solution(15), 0)
        self.assertEqual(solution(32), 0)

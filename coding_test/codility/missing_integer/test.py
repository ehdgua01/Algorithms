import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution([1, 3, 6, 4, 1, 2]), 5)
        self.assertEqual(solution([1, 2, 3]), 4)
        self.assertEqual(solution([-1, -3]), 1)
        self.assertEqual(solution([5]), 1)

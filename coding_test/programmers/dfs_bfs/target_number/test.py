import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution([1, 1, 1, 1, 1], 3), 5)
        self.assertEqual(solution([1, 2], 4), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5], 15), 1)

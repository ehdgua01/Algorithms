import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(solution([2, 3, 1, 5]), 4)
        self.assertEqual(solution([1]), 2)
        self.assertEqual(solution([2]), 1)
        self.assertEqual(solution([]), 1)

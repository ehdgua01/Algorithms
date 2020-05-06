import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertEqual(solution([0, 0, 0], 1), [0, 0, 0])
        self.assertEqual(solution([1, 2, 3, 4], 4), [1, 2, 3, 4])

    def test_case_2(self) -> None:
        self.assertEqual(solution([], 39), [])
        self.assertEqual(solution([1], 5), [1])
        self.assertEqual(solution([1, 1, 2, 3, 5], 7), [3, 5, 1, 1, 2])

import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(solution([3, 0, 6, 1, 5]), 3)
        self.assertEqual(solution([4, 7, 5, 1, 2, 3, 8, 9, 14]), 5)
        self.assertEqual(solution([8, 7, 7, 6, 5, 5, 3, 0, 0, 0]), 5)

    def test_case_2(self) -> None:
        self.assertEqual(solution([350, 452, 877]), 3)

    def test_case_3(self) -> None:
        self.assertEqual(solution([0]), 0)
        self.assertEqual(solution([4]), 1)

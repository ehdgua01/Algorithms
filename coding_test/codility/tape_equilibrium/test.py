import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(solution([3, 1, 2, 4, 3]), 1)

    def test_case_2(self) -> None:
        self.assertEqual(solution([-2, -3, -4, -1]), 0)

    def test_case_3(self) -> None:
        self.assertEqual(solution([-2, 3, -4, 1]), 2)
        self.assertEqual(solution([-1000, 1000]), 2000)
        self.assertEqual(solution([-10, -20, -30, -40, 100]), 20)

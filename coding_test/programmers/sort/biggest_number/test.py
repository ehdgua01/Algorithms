import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(solution([6, 10, 2]), "6210")
        self.assertEqual(solution([3, 30, 34, 5, 9]), "9534330")
        self.assertEqual(solution([41, 3, 30, 34, 381, 5, 990, 9]), "999054138134330")
        self.assertEqual(solution([1000, 999, 999, 190, 20, 0]), "9999992019010000")
        self.assertEqual(solution([12, 121]), "12121")
        self.assertEqual(solution([21, 212]), "21221")
        self.assertEqual(solution([112, 12]), "12112")
        self.assertEqual(solution([0, 0, 1000, 0]), "1000000")
        self.assertEqual(solution([998, 9, 999]), "9999998")
        self.assertEqual(solution([20, 200, 20]), "2020200")

    def test_case_2(self) -> None:
        self.assertEqual(solution([0, 0, 0, 0]), "0")

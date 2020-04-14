import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(solution([1, 2, 3, 4, 5]), [1])
        self.assertEqual(solution([1, 3, 2, 4, 2]), [1, 2, 3])

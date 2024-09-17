import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]), 2)

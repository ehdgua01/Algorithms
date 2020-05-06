import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(solution([9, 3, 9, 3, 9, 7, 9]), 7)

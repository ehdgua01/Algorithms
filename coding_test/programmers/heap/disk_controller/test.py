import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution([[0, 3], [1, 9], [2, 6]]), 9)

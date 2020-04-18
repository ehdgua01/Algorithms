import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution(["I 16", "D 1"]), [0, 0])
        self.assertEqual(solution(["I 7", "I 5", "I -5", "D -1"]), [7, 5])

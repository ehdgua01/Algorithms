import unittest

from .pipe import solution


class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution("()(((()())(())()))(())"), 17)
        self.assertEqual(solution("()"), 0)
        self.assertEqual(solution("(())((()()))"), 8)

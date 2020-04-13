import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(solution("17"), 3)
        self.assertEqual(solution("011"), 2)

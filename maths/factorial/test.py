import unittest

from .factorial import factorial


class TestCase(unittest.TestCase):
    def test_factorial(self) -> None:
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(0), 1)

import unittest

from .fibonacci import fibonacci
from .matrix_fibonacci import matrix_fibonacci


class TestCase(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(8), 21)

    def test_matrix_fibonacci(self):
        self.assertEqual(matrix_fibonacci(100), 354224848179261915075)

import unittest

from .fibonacci import fibonacci
from .matrix_fibonacci import matrix_fibonacci
from .recursion_fibonacci import recursion_fibonacci


class TestCase(unittest.TestCase):
    def test_fibonacci(self) -> None:
        self.assertEqual(fibonacci(100), 354224848179261915075)

    def test_matrix_fibonacci(self) -> None:
        self.assertEqual(matrix_fibonacci(100), 354224848179261915075)

    def test_recursion_fibonacci(self) -> None:
        self.assertEqual(recursion_fibonacci(10), 55)

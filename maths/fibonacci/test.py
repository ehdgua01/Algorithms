import unittest

from .fibonacci import fibonacci
from .matrix_fibonacci import matrix_fibonacci
from .recursion_fibonacci import recursion_fibonacci


class TestCase(unittest.TestCase):
    def test_fibonacci(self) -> None:
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(100), 354224848179261915075)

    def test_matrix_fibonacci(self) -> None:
        self.assertEqual(matrix_fibonacci(0), 0)
        self.assertEqual(matrix_fibonacci(1), 1)
        self.assertEqual(matrix_fibonacci(2), 1)
        self.assertEqual(matrix_fibonacci(3), 2)
        self.assertEqual(matrix_fibonacci(4), 3)
        self.assertEqual(matrix_fibonacci(5), 5)
        self.assertEqual(matrix_fibonacci(100), 354224848179261915075)

    def test_recursion_fibonacci(self) -> None:
        self.assertEqual(recursion_fibonacci(0), 0)
        self.assertEqual(recursion_fibonacci(1), 1)
        self.assertEqual(recursion_fibonacci(2), 1)
        self.assertEqual(recursion_fibonacci(3), 2)
        self.assertEqual(recursion_fibonacci(4), 3)
        self.assertEqual(recursion_fibonacci(5), 5)
        self.assertEqual(recursion_fibonacci(10), 55)

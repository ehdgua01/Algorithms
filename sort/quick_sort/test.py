import unittest

from .quick_sort import quick_sort
from .shuffle import shuffle_quick_sort
from .random_pivot import random_pivot_quick_sort
from .median_of_three import median_of_three_quick_sort
from .stack import stack_quick_sort


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [1, 5, 3, 7, 8, 4, 6, 2, 9]

    def test_quick_sort(self) -> None:
        quick_sort(self.data, 0, len(self.data) - 1)
        self.assertEqual(self.data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_shuffle_quick_sort(self) -> None:
        shuffle_quick_sort(self.data)
        self.assertEqual(self.data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_random_pivot_quick_sort(self) -> None:
        random_pivot_quick_sort(self.data, 0, len(self.data) - 1)
        self.assertEqual(self.data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_median_of_three_quick_sort(self) -> None:
        median_of_three_quick_sort(self.data, 0, len(self.data) - 1)
        self.assertEqual(self.data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_stack_quick_sort(self) -> None:
        stack_quick_sort(self.data)
        self.assertEqual(self.data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

import unittest

from .quick_sort import quick_sort
from .shuffle_quick_sort import shuffle_quick_sort
from .random_pivot_quick_sort import random_pivot_quick_sort
from .median_of_three_quick_sort import median_of_three_quick_sort


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [1, 5, 3, 7, 8, 4, 6, 2, 9]

    def test_quick_sort(self):
        quick_sort(self.data, 0, len(self.data) - 1)
        self.assertEqual(self.data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_shuffle_quick_sort(self):
        shuffle_quick_sort(self.data)
        self.assertEqual(self.data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_random_pivot_quick_sort(self):
        random_pivot_quick_sort(self.data, 0, len(self.data) - 1)
        self.assertEqual(self.data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_median_of_three_quick_sort(self):
        median_of_three_quick_sort(self.data, 0, len(self.data) - 1)
        self.assertEqual(self.data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

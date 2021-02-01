import random
import unittest

from .median_of_three import median_of_three_quick_sort
from .quick_sort import quick_sort
from .random_pivot import random_pivot_quick_sort
from .shuffle import shuffle_quick_sort
from .stack import stack_quick_sort


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.unsorted = random.choices(range(1, 11), k=10)
        self.sorted = sorted(self.unsorted)

    def test_quick_sort(self) -> None:
        self.assertEqual(
            quick_sort(self.unsorted, 0, len(self.unsorted) - 1), self.sorted
        )

    def test_shuffle_quick_sort(self) -> None:
        self.assertEqual(shuffle_quick_sort(self.unsorted), self.sorted)

    def test_random_pivot_quick_sort(self) -> None:
        self.assertEqual(
            random_pivot_quick_sort(self.unsorted, 0, len(self.unsorted) - 1),
            self.sorted,
        )

    def test_median_of_three_quick_sort(self) -> None:
        self.assertEqual(
            median_of_three_quick_sort(self.unsorted, 0, len(self.unsorted) - 1),
            self.sorted,
        )

    def test_stack_quick_sort(self) -> None:
        self.assertEqual(stack_quick_sort(self.unsorted), self.sorted)

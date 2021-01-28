import unittest

from .selection_sort import selection_sort


class TestCase(unittest.TestCase):
    def test_bubble_sort(self) -> None:
        self.assertEqual(selection_sort([1]), [1])
        self.assertEqual(selection_sort([]), [])
        self.assertEqual(
            selection_sort([8, 9, 4, 1, 5, 6, 7, 2, 3]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        )
        self.assertEqual(
            selection_sort([1, 1, 2, 1, 2, 1, 2, 2, 1, 2]),
            [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        )

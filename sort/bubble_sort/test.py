import unittest

from .bubble_sort import bubble_sort


class TestCase(unittest.TestCase):
    def test_bubble_sort(self) -> None:
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(
            bubble_sort([8, 9, 4, 1, 5, 6, 7, 2, 3]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        )
        self.assertEqual(
            bubble_sort([1, 1, 2, 1, 2, 1, 2, 2, 1, 2]), [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        )

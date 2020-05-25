import unittest

from .shell_sort import shell_sort


class TestCase(unittest.TestCase):
    def test_insertion_sort(self) -> None:
        self.assertEqual(
            shell_sort([9, 8, 2, 1, 4, 3, 6, 7, 5]), [1, 2, 3, 4, 5, 6, 7, 8, 9],
        )
        self.assertEqual(
            shell_sort([1, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1, 1, 1, 1],
        )
        self.assertEqual(
            shell_sort([1, 1, 2, 1, 2, 1, 1, 2, 1]), [1, 1, 1, 1, 1, 1, 2, 2, 2],
        )

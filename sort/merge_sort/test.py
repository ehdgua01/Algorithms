import unittest

from .merge_sort import merge_sort


class TestCase(unittest.TestCase):
    def test_merge_sort(self) -> None:
        data = [0, 2, 5, 9, 3, 7, 4, 6, 8, 1]
        self.assertEqual(merge_sort(data, 0, len(data)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

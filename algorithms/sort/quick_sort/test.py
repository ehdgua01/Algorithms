import unittest

from .quick_sort import quick_sort


class TestCase(unittest.TestCase):
    def test_quick_sort(self):
        data = [1, 5, 3, 7, 8, 4, 6, 2, 9]
        quick_sort(data, 0, len(data) - 1)
        self.assertEqual(data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

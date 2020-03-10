import unittest

from .binary_search import binary_search


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20,
        ]

    def test_binary_search(self):
        self.assertIsNone(
            binary_search(self.data, len(self.data), 21)
        )
        self.assertEqual(
            binary_search(self.data, len(self.data), 13),
            13,
        )

import unittest

from .binary_search import binary_search


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        # fmt: off
        self.data = [
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20,
        ]
        # fmt: on

    def test_binary_search(self):
        self.assertRaises(
            Exception,
            binary_search,
            data=[1, 3, 2],
            size=3,
            target=2,
        )
        self.assertIsNone(binary_search(self.data, len(self.data), 21))
        self.assertEqual(
            binary_search(self.data, len(self.data), 13),
            13,
        )

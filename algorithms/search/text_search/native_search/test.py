import unittest
from string import ascii_lowercase

from .native_search import native_search


class TestCase(unittest.TestCase):
    def test_native_search(self):
        self.assertRaises(
            ValueError, native_search, text=ascii_lowercase, pattern="lmnop", offset=30
        )

        result = native_search(ascii_lowercase, "lmnop")
        self.assertEqual(
            result, {"start": 11, "end": 15, "match": "lmnop", "offset": 0},
        )
        self.assertEqual(ascii_lowercase[result["start"] : result["end"] + 1], "lmnop")

        result = native_search(ascii_lowercase, "lmnop", 10)
        self.assertEqual(
            result, {"start": 11, "end": 15, "match": "lmnop", "offset": 10},
        )
        self.assertEqual(ascii_lowercase[result["start"] : result["end"] + 1], "lmnop")

        result = native_search(ascii_lowercase, "lmnasdop")
        self.assertEqual(
            result, {"start": -1, "end": -1, "match": "", "offset": 0},
        )

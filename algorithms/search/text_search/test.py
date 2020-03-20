import unittest
from string import ascii_lowercase

from .native_search import native_search
from .rabin_karp import rabin_karp
from .knuth_morris_pratt import knuth_morris_pratt
from .boyer_moore import boyer_moore


class AbstractTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.func = None
        raise unittest.SkipTest

    def test_case_1(self) -> None:
        self.assertRaises(
            ValueError, self.func, text=ascii_lowercase, pattern="lmnop", offset=30
        )

        result = self.func(ascii_lowercase, "lmnop")
        self.assertEqual(
            result, {"start": 11, "end": 15, "match": "lmnop", "offset": 0},
        )
        self.assertEqual(ascii_lowercase[result["start"] : result["end"] + 1], "lmnop")

        result = self.func(ascii_lowercase, "lmnop", 10)
        self.assertEqual(
            result, {"start": 11, "end": 15, "match": "lmnop", "offset": 10},
        )
        self.assertEqual(ascii_lowercase[result["start"] : result["end"] + 1], "lmnop")

        result = self.func(ascii_lowercase, "lmnasdop")
        self.assertEqual(
            result, {"start": -1, "end": -1, "match": "", "offset": 0},
        )


class TestNativeSearch(AbstractTestCase):
    def setUp(self) -> None:
        self.func = native_search


class TestRabinKarp(AbstractTestCase):
    def setUp(self) -> None:
        self.func = rabin_karp


class TestKnuthMorrisPratt(AbstractTestCase):
    def setUp(self) -> None:
        self.func = knuth_morris_pratt


class TestBoyerMoore(AbstractTestCase):
    def setUp(self) -> None:
        self.func = boyer_moore

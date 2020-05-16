import unittest

from .gcd import gcd


class TestCase(unittest.TestCase):
    def test_gcd(self) -> None:
        self.assertEqual(gcd(11, 6), 1)
        self.assertEqual(gcd(5, 10), 5)
        self.assertEqual(gcd(6, 14), 2)

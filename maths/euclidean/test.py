import unittest

from .gcd import gcd
from .lcm import lcm
from .recursion_gcd import gcd as recursion_gcd


class TestCase(unittest.TestCase):
    def test_gcd(self) -> None:
        self.assertEqual(gcd(11, 6), 1)
        self.assertEqual(gcd(5, 10), 5)
        self.assertEqual(gcd(6, 14), 2)

    def test_lcm(self) -> None:
        self.assertEqual(lcm(11, 6), 66)
        self.assertEqual(lcm(5, 10), 10)
        self.assertEqual(lcm(4, 10), 20)

    def test_recursion_gcd(self) -> None:
        self.assertEqual(recursion_gcd(11, 6), 1)
        self.assertEqual(recursion_gcd(5, 10), 5)
        self.assertEqual(recursion_gcd(6, 14), 2)

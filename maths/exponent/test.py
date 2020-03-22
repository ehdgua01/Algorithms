import unittest

from .exponent import exponent_func


class TestCase(unittest.TestCase):
    def test_exponent(self):
        self.assertEqual(exponent_func(2, 10), 1024)

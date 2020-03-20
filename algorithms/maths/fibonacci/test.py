import unittest

from .fibonacci import fibonacci


class TestCase(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(8), 21)

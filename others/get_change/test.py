import unittest

from .get_change import get_change


class TestCase(unittest.TestCase):
    def test_assertion_error(self):
        self.assertRaises(AssertionError, get_change, price=2, pay=1)

    def test_get_change(self) -> None:
        self.assertEqual(get_change(500, 1000), {500: 1})
        self.assertEqual(get_change(500, 1234), {500: 1, 100: 2, 10: 3, 1: 4})
        self.assertEqual(get_change(1200, 2000), {500: 1, 100: 3})

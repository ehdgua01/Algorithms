import unittest

from .anagram import anagram


class TestCase(unittest.TestCase):
    def test_anagram(self) -> None:
        self.assertEqual(anagram("apple", "pplea"), True)
        self.assertEqual(anagram("soccer", "o cc er s"), True)
        self.assertEqual(anagram("abc", "ddd"), False)

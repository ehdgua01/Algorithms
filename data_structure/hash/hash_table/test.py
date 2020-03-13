import unittest

from .hash_table import HashTable


class TestCase(unittest.TestCase):
    def test_hash_table(self) -> None:
        hash_table = HashTable(1)
        hash_table[0] = 1
        self.assertEqual(hash_table[0], 1)

        self.assertRaises(ValueError, hash_table.resize, new_size=0)
        hash_table.resize(6)
        self.assertEqual(hash_table.size, 7)

        hash_table[92] = 12
        self.assertEqual(hash_table[92], 12)

import unittest

from .division_method import DivisionMethodHashTable
from .digits_folding import DigitsFoldingHashTable
from .linked_list_hash_table import LinkedListHashTable


class TestCase(unittest.TestCase):
    def test_division_method(self) -> None:
        hash_table = DivisionMethodHashTable(3)

        hash_table[1] = 1
        hash_table[2] = 2
        hash_table[3] = 3
        hash_table[4] = 12

        self.assertEqual(hash_table[1], 12)  # Collision
        self.assertEqual(hash_table[2], 2)
        self.assertEqual(hash_table[3], 3)
        self.assertEqual(hash_table[4], 12)

    def test_digits_folding(self) -> None:
        hash_table = DigitsFoldingHashTable(1000)

        hash_table[0] = 1
        self.assertEqual(hash_table[0], 1)

        hash_table["test_key"] = "test_value"
        self.assertEqual(hash_table["test_key"], "test_value")

    def test_linked_list(self) -> None:
        hash_table = LinkedListHashTable(10)

        hash_table[12] = "A"
        self.assertEqual(hash_table[12], "A")
        hash_table[22] = "B"
        self.assertEqual(hash_table[22], "B")
        self.assertIsNone(hash_table[13])

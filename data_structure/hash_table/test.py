import unittest

from .division_method import DivisionMethodHashTable
from .digits_folding import DigitsFoldingHashTable
from .linked_list_hash_table import LinkedListHashTable
from .linear_probing import LinearProbingHashTable
from .quadratic_probing import QuadraticProbingHashTable


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

    def test_linear_probing(self) -> None:
        hash_table = LinearProbingHashTable(3)

        hash_table.set(1)
        hash_table.set(2)
        hash_table.set(3)
        self.assertEqual(hash_table.size, 3)

        hash_table.set(4)
        self.assertEqual(hash_table.size, 5)

        hash_table.set(5)
        hash_table.set(6)
        hash_table.set(7)
        self.assertEqual(hash_table.keys, {5: 5, 1: 1, 2: 2, 3: 3, 4: 4, 6: 6, 0: 7})
        self.assertEqual(hash_table.size, 7)

    def test_quadratic_probing(self) -> None:
        hash_table = QuadraticProbingHashTable(7)

        for i in range(0, 12, 2):
            hash_table.set(i)

        self.assertEqual(hash_table.size, 7)

        hash_table.set(14)
        self.assertEqual(hash_table.size, 11)
        self.assertEqual(hash_table.keys, {0: 0, 8: 8, 2: 2, 10: 10, 4: 4, 6: 6, 3: 14})

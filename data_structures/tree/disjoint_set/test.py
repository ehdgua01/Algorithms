import unittest

from .disjoint_set import DisjointSetNode


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.set_a = DisjointSetNode("Set A")
        self.set_c = DisjointSetNode("Set C")
        self.set_d = DisjointSetNode("Set D")
        self.set_b = DisjointSetNode("Set B")

    def test_disjoint_set(self) -> None:
        self.assertIsNot(
            self.set_a.find_set(), self.set_b.find_set(),
        )

        self.set_a.union(self.set_c)
        self.assertEqual(
            self.set_a.find_set(), self.set_c.find_set(),
        )

        self.assertIsNot(
            self.set_c.find_set(), self.set_d.find_set(),
        )

        self.set_c.union(self.set_d)
        self.assertEqual(
            self.set_a.find_set(), self.set_d.find_set(),
        )

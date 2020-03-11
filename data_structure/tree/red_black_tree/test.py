import unittest

from .red_black_tree import RedBlackTree


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.rbt = RedBlackTree()

    def test_red_black_tree(self) -> None:
        for i in range(300000):
            self.rbt.insert(i)

        self.assertIsNotNone(self.rbt.search(30300))
        self.assertIsNotNone(self.rbt.remove(30300))
        self.assertIsNone(self.rbt.search(30300))

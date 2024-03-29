import unittest

from .simple_binary_tree import (
    Node,
    destroy_tree,
    in_order_tree,
    is_full,
    post_order_tree,
    pre_order_tree,
)


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Node("A")
        self.node_b = Node("B")
        self.node_c = Node("C")
        self.node_d = Node("D")
        self.node_e = Node("E")
        self.node_f = Node("F")
        self.node_g = Node("G")

        self.root.left = self.node_b
        self.root.right = self.node_e
        self.node_b.left = self.node_c
        self.node_b.right = self.node_d
        self.node_e.left = self.node_f
        self.node_e.right = self.node_g

    def test_pre_order_tree(self):
        self.assertEqual(pre_order_tree(self.root), "ABCDEFG")

    def test_in_order_tree(self):
        self.assertEqual(in_order_tree(self.root), "CBDAFEG")

    def test_post_order_tree(self):
        self.assertEqual(post_order_tree(self.root), "CDBFGEA")

    def test_is_full_binary_tree(self):
        self.assertEqual(is_full(self.root), True)
        self.node_e.right = None
        self.assertEqual(is_full(self.root), False)

    def test_destroy_tree(self):
        destroy_tree(self.root)
        self.assertIsNone(self.root.left)
        self.assertIsNone(self.root.right)
        self.assertIsNone(self.node_b.left)
        self.assertIsNone(self.node_b.right)
        self.assertIsNone(self.node_c.left)
        self.assertIsNone(self.node_c.right)
        self.assertIsNone(self.node_d.left)
        self.assertIsNone(self.node_d.right)
        self.assertIsNone(self.node_e.left)
        self.assertIsNone(self.node_e.right)
        self.assertIsNone(self.node_f.left)
        self.assertIsNone(self.node_f.right)
        self.assertIsNone(self.node_g.left)
        self.assertIsNone(self.node_g.right)


if __name__ == "__main__":
    unittest.main()

import unittest

from .lcrs import Node, append, destroy, print_tree


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Node('Root')

    def test_lcrs(self):
        node_a = Node('A')
        node_b = Node('B')
        node_c = Node('C')
        node_d = Node('D')
        node_e = Node('E')

        append(self.root, node_a)
        self.assertEqual(self.root.child.value, 'A')
        self.assertIsNone(self.root.child.sibling)

        append(self.root, node_b)
        self.assertEqual(self.root.child.sibling.value, 'B')
        self.assertEqual(node_a.sibling, node_b)

        append(node_b, node_c)
        self.assertEqual(node_b.child.value, 'C')

        append(node_b, node_d)
        self.assertEqual(node_b.child.sibling.value, 'D')
        self.assertEqual(self.root.child.sibling.child.sibling.value, 'D')

        append(node_a, node_e)
        print_tree(self.root)
        """
        Root
        - A
        - - E
        - B
        - - C
        - - D
        """

        destroy(self.root)
        self.assertIsNone(self.root.child)
        self.assertIsNone(self.root.sibling)
        self.assertIsNone(node_a.child)
        self.assertIsNone(node_a.sibling)
        self.assertIsNone(node_b.child)
        self.assertIsNone(node_b.sibling)
        self.assertIsNone(node_c.child)
        self.assertIsNone(node_c.sibling)
        self.assertIsNone(node_d.child)
        self.assertIsNone(node_d.sibling)
        self.assertIsNone(node_e.child)
        self.assertIsNone(node_e.sibling)

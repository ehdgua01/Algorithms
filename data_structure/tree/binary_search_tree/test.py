import unittest

from .binary_search_tree import Node, BinarySearchTree


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20,
        ]

    def test_binary_search_tree(self):
        """
             D
           /  \
          B    F
         / \  / \
        A  C E  G
        """
        bst = BinarySearchTree()
        a = Node('A')
        b = Node('B')
        c = Node('C')
        d = Node('D')
        e = Node('E')
        f = Node('F')
        g = Node('G')

        # 삽입 알고리즘 테스트
        bst.insert(d)
        self.assertEqual(bst.root, d)

        bst.insert(b)
        self.assertEqual(bst.root.left, b)
        bst.insert(f)
        self.assertEqual(bst.root.right, f)

        bst.insert(a)
        self.assertEqual(bst.root.left.left, a)
        bst.insert(e)
        self.assertEqual(bst.root.right.left, e)

        bst.insert(c)
        self.assertEqual(bst.root.left.right, c)
        bst.insert(g)
        self.assertEqual(bst.root.right.right, g)

        # 탐색 알고리즘 테스트
        self.assertIsNone(bst.search('H'))
        self.assertEqual(bst.search('G', collection=bst.root), 'G')
        self.assertEqual(bst.search('D', collection=bst.root), 'D')
        self.assertEqual(bst.search('C', collection=bst.root), 'C')

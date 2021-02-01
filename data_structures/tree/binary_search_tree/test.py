import unittest

from .binary_search_tree import BinarySearchTree, Node


class TestCase(unittest.TestCase):
    def test_binary_search_tree(self):
        bst = BinarySearchTree()
        a = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        e = Node("E")
        f = Node("F")
        g = Node("G")

        # 삽입 알고리즘 테스트
        bst.insert(d)
        self.assertEqual(bst.root, d)
        self.assertIsNone(bst.root.parent)

        bst.insert(b)
        self.assertEqual(bst.root.left, b)
        self.assertEqual(b.parent, bst.root)
        bst.insert(f)
        self.assertEqual(bst.root.right, f)
        self.assertEqual(f.parent, bst.root)

        bst.insert(a)
        self.assertEqual(bst.root.left.left, a)
        self.assertEqual(a.parent, b)
        bst.insert(e)
        self.assertEqual(bst.root.right.left, e)
        self.assertEqual(e.parent, f)

        bst.insert(c)
        self.assertEqual(bst.root.left.right, c)
        self.assertEqual(c.parent, b)
        bst.insert(g)
        self.assertEqual(bst.root.right.right, g)
        self.assertEqual(g.parent, f)

        # 탐색 알고리즘 테스트
        self.assertIsNone(bst.search("H"))
        self.assertEqual(bst.search("G", collection=bst.root), g)
        self.assertEqual(bst.search("D", collection=bst.root), d)
        self.assertEqual(bst.search("C", collection=bst.root), c)

        # 제거 알고리즘 테스트
        bst.remove("F")
        self.assertEqual(bst.root.right, g)
        self.assertEqual(bst.root.right.left, e)

        # 루트 노드 제거 테스트
        bst.remove("D")
        self.assertEqual(bst.root, e)
        self.assertEqual(bst.root.right, g)
        self.assertEqual(bst.root.left, b)

        # 잎 노드 제거 테스트
        bst.remove("C")
        self.assertIsNone(bst.root.left.right)
        self.assertEqual(bst.root.left, b)

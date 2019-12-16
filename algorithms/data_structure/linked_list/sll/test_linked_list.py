import unittest
from .linked_list import LinkedList, Node


class TestCase(unittest.TestCase):
    sll = LinkedList()

    def test_append(self):
        self.sll.append(Node('append1'))
        self.assertEqual(self.sll.head.data, 'append1')
        self.assertEqual(self.sll.head.next_node, None)
        self.assertIs(self.sll.head, self.sll.pointer)
        self.assertEqual(self.sll.size, 1)

    def test_insert(self):
        self.sll.insert(Node('insert1'))
        self.assertEqual(self.sll.pointer.next_node.data, 'insert1')
        self.assertEqual(self.sll.size, 2)

        self.sll.insert(Node('insert_head'), True)
        self.assertEqual(self.sll.head.data, 'insert_head')
        self.assertEqual(self.sll.head.next_node.data, 'append1')
        self.assertEqual(self.sll.size, 3)

    def test_pop(self):
        result = self.sll.pop()
        self.assertEqual(result, 'insert1')
        self.assertEqual(self.sll.pointer.data, 'append1')
        self.assertIs(self.sll.tail, self.sll.pointer)
        self.assertEqual(self.sll.size, 2)

    def test_remove(self):
        self.sll.remove(self.sll.pointer)
        self.assertEqual(self.sll.pointer.data, 'insert_head')
        self.assertEqual(self.sll.size, 1)


if __name__ == '__main__':
    unittest.main()

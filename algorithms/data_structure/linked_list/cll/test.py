import unittest

from circular_linked_list import CircularLinkedList, Node


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.cll = CircularLinkedList()

    def test_append(self):
        self.cll.append(Node(1))
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.tail.data, 1)
        self.assertEqual(self.cll.tail.next.data, 1)
        self.assertEqual(self.cll.head.prev.data, 1)

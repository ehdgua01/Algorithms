import unittest

from .linear_search import linear_search
from .move_to_front import (
    move_to_front, linked_list_move_to_front,
    Node,
)


class TestCase(unittest.TestCase):
    def test_linear_search(self):
        self.assertEqual(
            linear_search([1, 2, 3], 2),
            2,
        )

    def test_move_to_front(self):
        data = [1, 2, 3]
        result = move_to_front(data, 3)
        self.assertEqual(result, 3)
        self.assertEqual(data[0], 3)
        self.assertEqual(data[1], 1)

    def test_linked_list_move_to_front(self):
        a = Node('A')
        b = Node('B')
        c = Node('C')
        head = a
        a.next = b
        b.next = c

        head = linked_list_move_to_front(head, 'C')
        self.assertEqual(head.value, 'C')
        self.assertEqual(head.next, a)
        self.assertEqual(a.next, b)

        head = linked_list_move_to_front(head, 'B')
        self.assertEqual(head.value, 'B')
        self.assertEqual(head.next, c)
        self.assertEqual(c.next, a)

import unittest

from .linear_search import linear_search
from .move_to_front import (
    move_to_front, linked_list_move_to_front,
    Node,
)
from .transpose import transpose_linear_search


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [1, 5, 4, 6, 2, 3]

    def test_linear_search(self) -> None:
        self.assertEqual(linear_search(self.data, 2), 2)

    def test_move_to_front(self) -> None:
        result = move_to_front(self.data, 3)
        self.assertEqual(result, 3)
        self.assertEqual(self.data[0], 3)
        self.assertEqual(self.data[1], 1)

    def test_linked_list_move_to_front(self) -> None:
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

    def test_transpose(self) -> None:
        self.assertEqual(self.data[3], 6)
        result = transpose_linear_search(self.data, 6)
        self.assertEqual(result, 6)
        self.assertEqual(self.data[2], 6)

        transpose_linear_search(self.data, 6)
        self.assertEqual(self.data[1], 6)

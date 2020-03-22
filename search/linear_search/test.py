import unittest

from .linear_search import linear_search
from .move_to_front import move_to_front
from .linked_list_move_to_front import linked_list_move_to_front, Node
from .transpose import transpose_linear_search
from .linked_list_transpose import linked_list_transpose


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [1, 5, 4, 6, 2, 3]
        self.a = Node("A")
        self.b = Node("B")
        self.c = Node("C")
        self.a.next = self.b
        self.b.next = self.c

    def test_linear_search(self) -> None:
        self.assertEqual(linear_search(self.data, 2), 2)

    def test_move_to_front(self) -> None:
        result = move_to_front(self.data, 3)
        self.assertEqual(result, 3)
        self.assertEqual(self.data[0], 3)
        self.assertEqual(self.data[1], 1)

        self.assertIsNone(move_to_front(self.data, 7))

    def test_linked_list_move_to_front(self) -> None:
        head = linked_list_move_to_front(self.a, "C")
        self.assertEqual(head.value, "C")
        self.assertEqual(head.next, self.a)
        self.assertEqual(self.a.next, self.b)

        head = linked_list_move_to_front(head, "B")
        self.assertEqual(head.value, "B")
        self.assertEqual(head.next, self.c)
        self.assertEqual(self.c.next, self.a)

        self.assertIsNone(linked_list_move_to_front(self.a, "D"))

    def test_transpose(self) -> None:
        self.assertEqual(self.data[3], 6)
        result = transpose_linear_search(self.data, 6)
        self.assertEqual(result, 6)
        self.assertEqual(self.data[2], 6)

        transpose_linear_search(self.data, 6)
        self.assertEqual(self.data[1], 6)

        self.assertIsNone(transpose_linear_search(self.data, 8))

    def test_linked_list_transpose(self) -> None:
        result = linked_list_transpose(self.a, "B")
        self.assertEqual(result.value, "B")
        self.assertEqual(self.b.next, self.a)
        self.assertEqual(self.a.next, self.c)

        result = linked_list_transpose(self.b, "C")
        self.assertEqual(result.value, "C")
        self.assertEqual(self.b.next, self.c)
        self.assertEqual(self.c.next, self.a)
        self.assertIsNone(self.a.next)

        self.assertIsNone(linked_list_transpose(self.b, "D"))

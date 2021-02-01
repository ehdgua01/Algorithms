import unittest

from .singly_linked_list import Node, SinglyLinkedList


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sll = SinglyLinkedList()

    def test_append(self):
        self.sll.append(Node(1))
        self.assertEqual(self.sll.head.data, 1)
        self.assertEqual(self.sll.head.next, None)
        self.assertEqual(self.sll.tail.data, 1)
        self.assertEqual(self.sll.tail.next, None)
        self.assertEqual(self.sll.size, 1)

        self.sll.append(Node(2))
        self.assertEqual(self.sll.head.data, 1)
        self.assertEqual(self.sll.head.next.data, 2)
        self.assertEqual(self.sll.tail.data, 2)
        self.assertEqual(self.sll.tail.next, None)
        self.assertEqual(self.sll.size, 2)

        self.sll.append(Node(3))
        self.assertEqual(self.sll.head.data, 1)
        self.assertEqual(self.sll.head.next.data, 2)
        self.assertEqual(self.sll.head.next.next.data, 3)
        self.assertEqual(self.sll.tail.data, 3)
        self.assertEqual(self.sll.tail.next, None)
        self.assertEqual(self.sll.size, 3)

    def test_get_data_at(self):
        self.assertRaises(ValueError, self.sll.get_data_at, location=1)
        for i in range(1, 11):
            self.sll.append(Node(i))
        self.assertEqual(self.sll.get_data_at(1), 1)
        self.assertEqual(self.sll.get_data_at(4), 4)
        self.assertEqual(self.sll.get_data_at(9), 9)

    def test_insert(self):
        self.sll.insert(Node(1), 1)
        self.assertEqual(self.sll.size, 1)
        self.assertEqual(self.sll.head.data, 1)
        self.assertEqual(self.sll.tail.data, 1)

        self.sll.insert(Node(2), 1)
        self.assertEqual(self.sll.size, 2)
        self.assertEqual(self.sll.get_data_at(2), 2)
        self.assertEqual(self.sll.tail.data, 2)

        self.sll.insert(Node(3), 1)
        self.assertEqual(self.sll.size, 3)
        self.assertEqual(self.sll.get_data_at(2), 3)
        self.assertEqual(self.sll.tail.data, 2)

        self.sll.insert(Node(4), 3)
        self.assertEqual(self.sll.size, 4)
        self.assertEqual(self.sll.get_data_at(3), 2)
        self.assertEqual(self.sll.get_data_at(4), 4)
        self.assertEqual(self.sll.tail.data, 4)

    def test_pop(self):
        self.assertRaises(ValueError, self.sll.pop)
        for i in range(1, 11):
            self.sll.append(Node(i))
        self.sll.pop()
        self.assertEqual(self.sll.tail.data, 9)
        self.assertEqual(self.sll.size, 9)
        self.sll.pop()
        self.assertEqual(self.sll.tail.data, 8)
        self.assertEqual(self.sll.size, 8)

    def test_remove(self):
        self.assertRaises(ValueError, self.sll.remove, location=1)
        for i in range(1, 11):
            self.sll.append(Node(i))
        self.sll.remove(7)
        self.assertEqual(self.sll.get_data_at(7), 8)
        self.assertEqual(self.sll.get_data_at(8), 9)
        self.assertEqual(self.sll.size, 9)
        self.sll.remove(3)
        self.assertEqual(self.sll.get_data_at(3), 4)
        self.assertEqual(self.sll.size, 8)


if __name__ == "__main__":
    unittest.main()

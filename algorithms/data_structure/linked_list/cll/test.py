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
        self.assertEqual(self.cll.size, 1)

        self.cll.append(Node(2))
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.tail.data, 2)
        self.assertEqual(self.cll.tail.next.data, 1)
        self.assertEqual(self.cll.head.prev.data, 2)
        self.assertEqual(self.cll.size, 2)

        self.cll.append(Node(3))
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.tail.data, 3)
        self.assertEqual(self.cll.tail.next.data, 1)
        self.assertEqual(self.cll.head.prev.data, 3)
        self.assertEqual(self.cll.size, 3)

    def test_get_data_at(self):
        for i in range(1, 11):
            self.cll.append(Node(i))
        self.assertEqual(self.cll.get_data_at(3), 3)
        self.assertEqual(self.cll.get_data_at(7), 7)
        self.assertEqual(self.cll.get_data_at(10), 10)

    def test_insert(self):
        self.cll.insert(Node(1), 1)
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.tail.data, 1)
        self.assertEqual(self.cll.tail.next.data, 1)
        self.assertEqual(self.cll.head.prev.data, 1)
        self.assertEqual(self.cll.size, 1)

        self.cll.insert(Node(2), 1)
        self.assertEqual(self.cll.tail.data, 2)
        self.assertEqual(self.cll.tail.next.data, 1)
        self.assertEqual(self.cll.head.prev.data, 2)
        self.assertEqual(self.cll.size, 2)

        self.cll.insert(Node(3), 2)
        self.assertEqual(self.cll.tail.data, 3)
        self.assertEqual(self.cll.tail.next.data, 1)
        self.assertEqual(self.cll.head.prev.data, 3)
        self.assertEqual(self.cll.size, 3)

        self.cll.insert(Node(4), 2)
        self.assertEqual(self.cll.tail.data, 3)
        self.assertEqual(self.cll.tail.next.data, 1)
        self.assertEqual(self.cll.get_data_at(3), 4)
        self.assertEqual(self.cll.size, 4)

    def test_pop(self):
        self.assertRaises(ValueError, self.cll.pop)

        for i in range(1, 11):
            self.cll.append(Node(i))

        self.cll.pop()
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.tail.data, 9)
        self.cll.pop()
        self.assertEqual(self.cll.tail.data, 8)
        self.cll.pop()
        self.assertEqual(self.cll.tail.data, 7)

    def test_remove(self):
        self.assertRaises(ValueError, self.cll.remove, location=0)

        for i in range(1, 11):
            self.cll.append(Node(i))

        self.cll.remove(3)
        self.assertEqual(self.cll.get_data_at(3), 4)
        self.assertEqual(self.cll.tail.data, 10)
        self.assertEqual(self.cll.size, 9)

        self.cll.remove(9)
        self.assertEqual(self.cll.get_data_at(8), 9)
        self.assertEqual(self.cll.tail.data, 9)
        self.assertEqual(self.cll.size, 8)

        self.cll.remove(1)
        self.assertEqual(self.cll.head.prev, self.cll.tail)
        self.assertEqual(self.cll.head.data, 2)


if __name__ == '__main__':
    unittest.main()

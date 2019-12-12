import unittest

from doubly_linked_list import DoublyLinkedList, Node


class TestCase(unittest.TestCase):
    dll = None

    def setUp(self) -> None:
        self.dll = DoublyLinkedList()

    def test_is_empty(self):
        self.assertEqual(self.dll.is_empty, True)

    def test_append_and_pop(self):
        self.dll.append(Node(1))
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 1)
        self.assertEqual(self.dll.size, 1)

        self.dll.append(Node(2))
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.tail.data, 2)
        self.assertEqual(self.dll.size, 2)

        self.dll.append(Node(3))
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 3)
        self.assertEqual(self.dll.size, 3)

        self.dll.pop()
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.tail.data, 2)
        self.assertEqual(self.dll.size, 2)

        self.dll.pop()
        self.assertEqual(self.dll.head.next, None)
        self.assertEqual(self.dll.tail.data, 1)
        self.assertEqual(self.dll.size, 1)

    def test_get_data_at(self):
        self.assertRaises(ValueError, self.dll.get_data_at, location=1)

        for i in range(1, 11):
            self.dll.append(Node(i))

        self.assertEqual(self.dll.get_data_at(1), 1)
        self.assertEqual(self.dll.get_data_at(4), 4)
        self.assertEqual(self.dll.get_data_at(8), 8)

    def test_insert(self):
        self.assertRaises(
            ValueError,
            self.dll.insert,
            new=Node(1),
            location=-2
        )
        self.dll.insert(Node(1), 1)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 1)
        self.assertEqual(self.dll.size, 1)

        self.dll.insert(Node(2), 1)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.tail.data, 2)
        self.assertEqual(self.dll.size, 2)

        self.dll.insert(Node(3), 2)
        self.assertEqual(self.dll.get_data_at(2), 2)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.tail.prev.data, 2)
        self.assertEqual(self.dll.tail.data, 3)
        self.assertEqual(self.dll.size, 3)

        self.dll.insert(Node(4), 2)
        self.assertEqual(self.dll.get_data_at(3), 4)
        self.assertEqual(self.dll.tail.prev.data, 4)
        # test git commit time
        self.assertEqual(self.dll.size, 4)

    def test_remove(self):
        self.assertRaises(ValueError, self.dll.remove, location=0)

        for i in range(1, 11):
            self.dll.append(Node(i))

        self.dll.remove(2)
        self.assertEqual(self.dll.get_data_at(1), 1)
        self.assertEqual(self.dll.get_data_at(2), 3)
        self.assertEqual(self.dll.get_data_at(3), 4)
        self.assertEqual(self.dll.size, 9)

        self.dll.remove(5)
        self.assertEqual(self.dll.get_data_at(4), 5)
        self.assertEqual(self.dll.get_data_at(5), 7)
        self.assertEqual(self.dll.get_data_at(6), 8)
        self.assertEqual(self.dll.size, 8)


if __name__ == '__main__':
    unittest.main()

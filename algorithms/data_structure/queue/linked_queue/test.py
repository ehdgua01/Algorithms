import unittest

from linked_queue import LinkedQueue, Node


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = LinkedQueue()

    def test_all(self):
        self.assertEqual(self.queue.is_empty, True)
        self.assertRaises(Exception, self.queue.get)

        self.queue.put(Node(1))
        self.assertEqual(self.queue.is_empty, False)
        self.assertEqual(self.queue.size, 1)
        self.assertEqual(self.queue.front.value, 1)
        self.assertEqual(self.queue.rear.value, 1)

        self.queue.put(Node(2))
        self.assertEqual(self.queue.size, 2)
        self.assertEqual(self.queue.front.next.value, 2)
        self.assertEqual(self.queue.rear.value, 2)
        self.assertIsNone(self.queue.rear.next)

        self.queue.put(Node(3))
        self.assertEqual(self.queue.size, 3)
        self.assertEqual(self.queue.front.next.value, 2)
        self.assertEqual(self.queue.front.next.next.value, 3)
        self.assertEqual(self.queue.rear.value, 3)

        self.assertEqual(self.queue.get(), 1)
        self.assertEqual(self.queue.size, 2)
        self.assertEqual(self.queue.front.value, 2)
        self.assertEqual(self.queue.front.next.value, 3)
        self.assertEqual(self.queue.rear.value, 3)

        self.assertEqual(self.queue.get(), 2)
        self.assertEqual(self.queue.size, 1)
        self.assertEqual(self.queue.front.value, 3)
        self.assertIsNone(self.queue.front.next)
        self.assertEqual(self.queue.rear.value, 3)

        self.assertEqual(self.queue.get(), 3)
        self.assertEqual(self.queue.size, 0)
        self.assertEqual(self.queue.is_empty, True)
        self.assertIsNone(self.queue.front)
        self.assertIsNone(self.queue.rear)


if __name__ == '__main__':
    unittest.main()

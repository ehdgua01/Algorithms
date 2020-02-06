import unittest

from circular_queue import CircularQueue


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = CircularQueue(3)

    def test_all(self):
        self.assertEqual(self.queue.is_empty, True)
        self.assertEqual(self.queue.is_full, False)
        self.queue.put(1)
        self.assertEqual(self.queue.is_empty, False)
        self.assertEqual(self.queue.queue[0], 1)
        self.assertEqual(self.queue.rear, 1)
        self.queue.put(2)
        self.assertEqual(self.queue.queue[1], 2)
        self.assertEqual(self.queue.rear, 2)
        self.queue.put(3)
        self.assertEqual(self.queue.queue[2], 3)
        self.assertEqual(self.queue.rear, 3)
        self.assertEqual(self.queue.is_full, True)
        self.assertRaises(OverflowError, self.queue.put, 4)

        self.assertEqual(self.queue.get(), 1)
        self.assertEqual(self.queue.is_full, False)
        self.assertEqual(self.queue.front, 1)
        self.assertEqual(self.queue.queue[self.queue.front], 2)
        self.assertEqual(self.queue.get(), 2)
        self.assertEqual(self.queue.front, 2)
        self.assertEqual(self.queue.queue[self.queue.front], 3)
        self.assertEqual(self.queue.get(), 3)
        self.assertEqual(self.queue.front, 3)
        self.assertRaises(Exception, self.queue.get)
        self.assertEqual(self.queue.is_empty, True)

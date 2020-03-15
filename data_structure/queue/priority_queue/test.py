import unittest

from .priority_queue import PriorityQueue


class TestCase(unittest.TestCase):
    def test_priority_queue(self):
        queue = PriorityQueue()
        queue.enqueue(("First", 3))
        self.assertEqual(queue.size, 1)
        queue.enqueue(("Second", 2))
        self.assertEqual(queue.size, 2)
        queue.enqueue(("Third", 1))
        self.assertEqual(queue.size, 3)

        self.assertEqual(queue.dequeue(), ("Third", 1))
        self.assertEqual(queue.size, 2)
        self.assertEqual(queue.dequeue(), ("Second", 2))
        self.assertEqual(queue.size, 1)
        self.assertEqual(queue.dequeue(), ("First", 3))
        self.assertEqual(queue.size, 0)
        self.assertIsNone(queue.dequeue())

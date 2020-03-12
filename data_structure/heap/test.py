import unittest

from .heap import Heap


class TestCase(unittest.TestCase):
    def test_heap(self):
        heap = Heap()
        heap.insert(2)
        self.assertEqual(heap.get_data(0), 2)
        self.assertEqual(heap.size, 1)
        heap.insert(3)
        self.assertEqual(heap.get_data(1), 3)
        self.assertEqual(heap.size, 2)
        heap.insert(1)
        self.assertEqual(heap.get_data(0), 1)
        self.assertEqual(heap.size, 3)
        self.assertEqual(heap.get_data(2), 2)

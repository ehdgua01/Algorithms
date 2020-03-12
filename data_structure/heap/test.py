import unittest

from .min_heap import MinHeap


class TestCase(unittest.TestCase):
    def test_min_heap(self):
        heap = MinHeap()
        heap.insert(2)
        self.assertEqual(heap.data[0], 2)
        self.assertEqual(heap.size, 1)
        heap.insert(3)
        self.assertEqual(heap.data[1], 3)
        self.assertEqual(heap.size, 2)
        heap.insert(1)
        self.assertEqual(heap.data[0], 1)
        self.assertEqual(heap.size, 3)
        self.assertEqual(heap.data[2], 2)
        heap.remove_min()
        self.assertEqual(heap.data[0], 2)
        self.assertEqual(heap.data[1], 3)
        self.assertEqual(heap.size, 2)
        heap.remove_min()
        self.assertEqual(heap.data[0], 3)
        self.assertEqual(heap.size, 1)
        heap.remove_min()
        self.assertEqual(heap.size, 0)

        for i in range(300000):
            heap.insert(i)
        for _ in range(300000):
            heap.remove_min()

import unittest

from .insertion_sort import insertion_sort
from .linked_list_i_sort import linked_list_i_sort, Node


class TestCase(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(
            insertion_sort([9, 8, 2, 1, 4, 3, 6, 7, 5]), [1, 2, 3, 4, 5, 6, 7, 8, 9],
        )
        self.assertEqual(
            insertion_sort([1, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1, 1, 1, 1],
        )
        self.assertEqual(
            insertion_sort([1, 1, 2, 1, 2, 1, 1, 2, 1]), [1, 1, 1, 1, 1, 1, 2, 2, 2],
        )

    def test_linked_list_i_sort(self):
        unsorted = Node(1)
        unsorted.insert(Node(4))
        unsorted.insert(Node(6))
        unsorted.insert(Node(3))
        unsorted.insert(Node(5))
        unsorted.insert(Node(2))
        unsorted.insert(Node(8))
        unsorted.insert(Node(7))
        unsorted.insert(Node(9))

        linked_list_i_sort(unsorted)

        for i in range(1, 10):
            j = 1
            v = unsorted
            while j < i:
                v = v.next
                j += 1
            self.assertEqual(v.value, i)

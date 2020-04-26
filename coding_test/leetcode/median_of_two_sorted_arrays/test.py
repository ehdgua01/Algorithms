import unittest

from .solution import Solution


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1, 3], [2]), 2.0)

    def test_case_2(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

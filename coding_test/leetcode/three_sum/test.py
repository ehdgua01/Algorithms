import unittest

from .solution import Solution


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution().threeSum

    def test_case_1(self) -> None:
        self.assertEqual(self.solution([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])

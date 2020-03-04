import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(
            solution([1, 2, 3, 2, 3]),
            [4, 3, 1, 1, 0],
        )
        self.assertEqual(
            solution([0, 0, 0, 0, 0]),
            [4, 3, 2, 1, 0]
        )
        self.assertEqual(
            solution([9, 8, 7, 6, 5]),
            [1, 1, 1, 1, 0],
        )


if __name__ == '__main__':
    unittest.main()

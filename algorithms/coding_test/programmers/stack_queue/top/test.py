import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(
            solution([6, 9, 5, 7, 4]),
            [0, 0, 2, 2, 4],
        )
        self.assertEqual(
            solution([3, 9, 9, 3, 5, 7, 2]),
            [0, 0, 0, 3, 3, 3, 6],
        )
        self.assertEqual(
            solution([1, 5, 3, 6, 7, 6, 5]),
            [0, 0, 2, 0, 0, 5, 6],
        )


if __name__ == '__main__':
    unittest.main()

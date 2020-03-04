import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([2, 1, 3, 2], 2), 1)
        self.assertEqual(solution([1, 1, 9, 1, 1, 1], 0), 5)


if __name__ == '__main__':
    unittest.main()

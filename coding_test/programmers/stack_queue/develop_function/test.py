import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([99, 40, 30], [1, 20, 55]), [1, 2])


if __name__ == "__main__":
    unittest.main()

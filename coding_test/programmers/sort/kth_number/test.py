import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(
            solution(
                array=[1, 5, 2, 6, 3, 7, 4], commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]],
            ),
            [5, 6, 3],
        )


if __name__ == "__main__":
    unittest.main()

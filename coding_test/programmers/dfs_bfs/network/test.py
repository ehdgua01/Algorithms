import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
        self.assertEqual(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
        self.assertEqual(solution(3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 1)
        self.assertEqual(
            solution(4, [[1, 1, 1, 0], [1, 1, 0, 0], [1, 0, 1, 1], [0, 0, 1, 1]]), 1
        )
        self.assertEqual(
            solution(4, [[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]), 1
        )
        self.assertEqual(
            solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), 4
        )
        self.assertEqual(
            solution(4, [[1, 0, 0, 1], [0, 1, 1, 1], [0, 1, 1, 0], [1, 0, 1, 1]]), 1
        )
        self.assertEqual(
            solution(
                5,
                [
                    [1, 1, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 1],
                ],
            ),
            3,
        )

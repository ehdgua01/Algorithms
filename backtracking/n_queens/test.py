import unittest

from .n_queens import n_queens


class TestCase(unittest.TestCase):
    def test_2_3_queens(self) -> None:
        self.assertEqual(n_queens(2), [])
        self.assertEqual(n_queens(3), [])

    def test_4_queens(self) -> None:
        result = n_queens(4)
        self.assertEqual(
            result, [[(1, 0), (3, 1), (0, 2), (2, 3)], [(2, 0), (0, 1), (3, 2), (1, 3)]]
        )
        self.assertEqual(len(result), 2)

    def test_8_queens(self) -> None:
        result = n_queens(8)
        self.assertEqual(
            result[0], [(0, 0), (4, 1), (7, 2), (5, 3), (2, 4), (6, 5), (1, 6), (3, 7)],
        )
        self.assertEqual(len(result), 92)

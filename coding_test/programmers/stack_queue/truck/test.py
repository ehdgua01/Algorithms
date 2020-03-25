import unittest

from .solution import solution


class UnitTest(unittest.TestCase):
    def test_solution(self) -> None:
        self.assertEqual(
            solution(bridge_length=2, weight=10, truck_weights=[7, 4, 5, 6]), 8
        )
        self.assertEqual(
            solution(bridge_length=100, weight=100, truck_weights=[10]), 101,
        )
        self.assertEqual(
            solution(
                bridge_length=100,
                weight=100,
                truck_weights=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            ),
            110,
        )


if __name__ == "__main__":
    unittest.main()

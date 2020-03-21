import unittest
from typing import List

from .simple_lcs import simple_lcs
from .lcs import lcs


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.first_string: str = "GOOD MORNING"
        self.second_string: str = "GUTEN MORGEN"
        self.result_matrix: List[List[int]] = [
            [0] * (len(self.second_string) + 1)
            for _ in range(len(self.first_string) + 1)
        ]

    def test_simple_lcs(self) -> None:
        self.assertEqual(
            simple_lcs(
                self.first_string,
                self.second_string,
                len(self.first_string),
                len(self.second_string),
                self.result_matrix,
            ),
            6,
        )

    def test_lcs(self) -> None:
        self.assertEqual(
            lcs(
                self.first_string,
                self.second_string,
                len(self.first_string),
                len(self.second_string),
                self.result_matrix,
            ),
            6,
        )

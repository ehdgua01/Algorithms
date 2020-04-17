import unittest

from .solution import solution


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]),
            ["ICN", "JFK", "HND", "IAD"],
        )
        self.assertEqual(
            solution(
                [
                    ["ICN", "SFO"],
                    ["ICN", "ATL"],
                    ["SFO", "ATL"],
                    ["ATL", "ICN"],
                    ["ATL", "SFO"],
                ]
            ),
            ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"],
        )

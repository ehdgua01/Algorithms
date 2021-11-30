from .solution import Solution


def test_solution():
    solution = Solution().intToRoman
    assert solution(4) == "IV"
    assert solution(9) == "IX"
    assert solution(58) == "LVIII"
    assert solution(1994) == "MCMXCIV"

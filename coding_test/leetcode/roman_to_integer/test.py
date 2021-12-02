from .solution import Solution


def test_solution():
    solution = Solution().romanToInt
    assert solution("IV") == 4
    assert solution("IX") == 9
    assert solution("LVIII") == 58
    assert solution("MCMXCIV") == 1994
    assert solution("CM") == 900

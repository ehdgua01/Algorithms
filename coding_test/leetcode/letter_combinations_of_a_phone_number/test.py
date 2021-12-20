from .solution import Solution


def test_solution():
    letter_combinations = Solution().letterCombinations
    assert letter_combinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]
    assert letter_combinations("") == []
    assert letter_combinations("2") == ["a", "b", "c"]

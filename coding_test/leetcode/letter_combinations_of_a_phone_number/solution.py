from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def make_combinations(pos: int, current: List[str]):
            if pos == len(digits):
                result.append("".join(current))
                return
            for char in mapping[digits[pos]]:
                current.append(char)
                make_combinations(pos + 1, current)
                current.pop()

        result = []
        make_combinations(0, [])
        return result

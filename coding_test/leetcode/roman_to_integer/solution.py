class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        result = 0
        for i, roman in enumerate(s[:-1]):
            if symbols[s[i]] < symbols[s[i + 1]]:
                result -= symbols[s[i]]
            else:
                result += symbols[s[i]]
        result += symbols[s[-1]]
        return result

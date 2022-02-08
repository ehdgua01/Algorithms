class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0


def test_solution():
    add_digits = Solution().addDigits
    assert add_digits(38) == 2
    assert add_digits(0) == 0

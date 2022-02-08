class Solution:
    def addDigits(self, num: int) -> int:
        sum_ = sum(map(int, str(num)))
        if sum_ < 10:
            return sum_
        else:
            return self.addDigits(sum_)


def test_solution():
    add_digits = Solution().addDigits
    assert add_digits(38) == 2
    assert add_digits(0) == 0

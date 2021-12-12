import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def fulfill(num) -> bool:
            total = (
                num // a
                + num // b
                + num // c
                - num // ab
                - num // ac
                - num // bc
                + num // abc
            )
            return total >= n

        def lcm(x, y) -> int:
            return x * y // math.gcd(x, y)

        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(a, bc)

        left, right = 1, n * min(a, b, c)
        while left < right:
            mid = left + (right - left) // 2
            if fulfill(mid):
                right = mid
            else:
                left = mid + 1
        return left

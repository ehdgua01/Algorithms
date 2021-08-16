class Solution:
    def reverse(self, x: int) -> int:
        int32 = 2 ** 31
        r = int(str(abs(x))[::-1])
        if -int32 <= r < int32:
            return -r if x < 0 else r
        return 0

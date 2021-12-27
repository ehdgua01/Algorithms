class Solution:
    def findComplement(self, num: int) -> int:
        xor = 0
        for x in range(len(bin(num)) - 2):
            xor = xor << 1
            xor = xor | 1
        return num ^ xor


def test_solution():
    find_complement = Solution().findComplement
    assert find_complement(5) == 2
    assert find_complement(1) == 0

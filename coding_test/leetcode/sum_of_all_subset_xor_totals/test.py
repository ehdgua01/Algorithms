from functools import reduce
from itertools import combinations
from operator import xor
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return sum(reduce(xor, c) for i in range(1, len(nums) + 1) for c in combinations(nums, i))


def test_subsetXORSum():
    s = Solution()
    assert s.subsetXORSum([1, 3]) == 6
    assert s.subsetXORSum([5, 1, 6]) == 28
    assert s.subsetXORSum([3, 4, 5, 6, 7, 8]) == 480

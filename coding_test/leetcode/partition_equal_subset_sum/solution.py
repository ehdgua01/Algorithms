from typing import List


class Solution:
    def canPartition(self, nums: List[int]):
        total_sum = sum(nums)
        if total_sum & 1:
            return False
        half_sum, dp = total_sum // 2, 1
        for num in nums:
            dp |= dp << num
        return dp & 1 << half_sum

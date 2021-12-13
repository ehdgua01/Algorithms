from typing import List


class Solution:
    def canPartition(self, nums: List[int]):
        total_sum = sum(nums)
        if total_sum & 1:
            return False
        half_sum = total_sum // 2
        dp = [True] + [False] * half_sum
        for num in nums:
            for j in range(half_sum, num - 1, -1):
                dp[j] |= dp[j - num]
        return dp[half_sum]

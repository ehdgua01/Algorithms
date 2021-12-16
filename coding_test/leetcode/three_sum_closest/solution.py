from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        gap = 1000
        closest = 0
        for x in range(len(nums) - 2):
            y = x + 1
            z = len(nums) - 1
            while y < z:
                three_sum = nums[x] + nums[y] + nums[z]
                if abs(three_sum - target) < gap:
                    gap = abs(three_sum - target)
                    closest = three_sum
                if three_sum > target:
                    z -= 1
                elif three_sum < target:
                    y += 1
                else:
                    return three_sum
        return closest

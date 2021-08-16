from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, v in enumerate(nums):
            if target - v in values:
                return [values[target - v], i]
            else:
                values[v] = i

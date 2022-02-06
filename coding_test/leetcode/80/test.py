from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2, 0, -1):
            if nums[i] == nums[i - 1] == nums[i + 1]:
                nums.pop(i + 1)
        return len(nums)


def test_solution():
    remove_duplicates = Solution().removeDuplicates
    assert remove_duplicates([1, 1, 1, 2, 2, 3]) == 5
    assert remove_duplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7

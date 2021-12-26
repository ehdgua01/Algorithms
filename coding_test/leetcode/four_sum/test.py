from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    four_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if four_sum == target:
                        result.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
                    elif four_sum < target:
                        c += 1
                    else:
                        d -= 1
        return [list(it) for it in result]


def test_solution():
    four_sum = Solution().fourSum
    assert four_sum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2],
        [-1, 0, 0, 1],
        [-2, 0, 0, 2],
    ]
    assert four_sum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    assert four_sum([-3, -1, 0, 2, 4, 5], 1) == [[-3, -1, 0, 5]]

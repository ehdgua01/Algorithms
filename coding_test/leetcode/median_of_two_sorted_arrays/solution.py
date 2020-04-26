from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = sorted(nums1 + nums2)
        q, r = divmod(len(nums1), 2)
        return nums1[q] if r else (nums1[q] + nums1[q - 1]) / 2

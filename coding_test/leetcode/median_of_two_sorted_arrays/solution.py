from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = 0, 0
        i, j, h = 0, 0, (len(nums1) + len(nums2)) // 2

        while i + j <= h:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    a, b = b, nums1[i]
                    i += 1
                else:
                    a, b = b, nums2[j]
                    j += 1
            elif i < len(nums1):
                a, b = b, nums1[i]
                i += 1
            else:
                a, b = b, nums2[j]
                j += 1
        return b if (len(nums1) + len(nums2)) % 2 == 1 else (a + b) / 2

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if n < m:
            nums1, nums2, m, n = nums2, nums1, n, m

        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1
            elif 0 < i and nums2[j] < nums1[i - 1]:
                imax = i - 1
            else:
                max_left = max(nums1[i - 1], nums2[j - 1]) if i and j else nums1[i - 1] if i else nums2[j - 1]

                if (m + n) % 2 == 1:
                    return max_left

                min_right = min(nums1[i], nums2[j]) if i != m and j != n else nums2[j] if i == m else nums1[i]
                return (max_left + min_right) / 2

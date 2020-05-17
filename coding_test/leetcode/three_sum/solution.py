from typing import List
from collections import Counter


class Solution:
    def threeSum(self, nums: List) -> List[List[int]]:
        res = []
        lookup = Counter(nums)

        if 0 in lookup and lookup[0] > 2:
            res.append([0, 0, 0])

        negative, positive = [], []

        for n in lookup:
            if n < 0:
                negative.append(n)
            elif 0 < n:
                positive.append(n)

        for n in negative:
            for p in positive:
                sum_ = -p - n

                if sum_ not in lookup:
                    continue

                if sum_ == 0:
                    res.append([n, sum_, p])
                elif sum_ < n:
                    res.append([sum_, n, p])
                elif sum_ > p:
                    res.append([n, p, sum_])
                elif sum_ == n and lookup[sum_] > 1:
                    res.append([n, n, p])
                elif sum_ == p and lookup[sum_] > 1:
                    res.append([n, p, p])
        return res

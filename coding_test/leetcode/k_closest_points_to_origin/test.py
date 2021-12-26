import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=self.get_distance)

    def get_distance(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2


def test_solution():
    k_closest = Solution().kClosest
    assert k_closest([[1, 3], [-2, 2]], 1)

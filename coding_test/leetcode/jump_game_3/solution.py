from typing import List


class Solution:
    def __init__(self):
        self.result = False

    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [0] * len(arr)
        queue = [start]
        while queue:
            i = queue.pop()
            if arr[i] == 0:
                return True

            visited[i] = 1
            left = i - arr[i]
            if left >= 0 and visited[left] == 0:
                queue.append(left)

            right = i + arr[i]
            if right < len(arr) and visited[right] == 0:
                queue.append(right)
        return False

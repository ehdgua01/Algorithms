from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        stack = []

        def backtrack(i: int):
            if i >= len(candidates):
                return

            value = sum(stack)

            if value == target:
                result.append(stack[:])
                return

            if value < target:
                stack.append(candidates[i])
                backtrack(i)
                stack.pop()
                backtrack(i + 1)

        backtrack(0)
        return result


def test_combination_sum():
    s = Solution()

    def assert_(a, b):
        assert sorted(a) == sorted(b)

    assert_(s.combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
    assert_(s.combinationSum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    assert_(s.combinationSum([2], 1), [])

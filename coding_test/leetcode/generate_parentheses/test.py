from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(opened: int, closed: int):
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return res


def test():
    sol = Solution()
    assert sorted(sol.generateParenthesis(1)) == sorted(
        [
            "()",
        ]
    )
    assert sorted(sol.generateParenthesis(2)) == sorted(
        [
            "(())",
            "()()",
        ]
    )
    assert sorted(sol.generateParenthesis(3)) == sorted(
        [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()",
        ]
    )

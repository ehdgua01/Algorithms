class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


def test_solution():
    remove_duplicates = Solution().removeDuplicates
    assert remove_duplicates("abbaca") == "ca"
    assert remove_duplicates("azxxzy") == "ay"

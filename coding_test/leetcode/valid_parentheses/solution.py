class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_chars = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in open_chars:
                stack.append(char)
            elif not stack or open_chars[stack.pop()] != char:
                return False
        return not stack

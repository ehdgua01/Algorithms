class Solution:
    def maxPower(self, s: str) -> int:
        max_ = temp = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                temp += 1
                max_ = max(max_, temp)
            else:
                temp = 1
        return max_

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""
        start, end = 0, 0

        for i in range(len(s)):
            len_ = max(
                self.expand_around_center(s, i, i),
                self.expand_around_center(s, i, i + 1),
            )
            if end - start < len_:
                start = i - ((len_ - 1) // 2)
                end = i + (len_ // 2)
        return s[start : end + 1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

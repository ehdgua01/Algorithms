class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0 if len(s) < 1 else 1
        i = 0
        temp_s = ""

        while i < len(s) - 1:
            for i in range(i, len(s)):
                if s[i] in temp_s:
                    break
                temp_s += s[i]
            if answer < len(temp_s):
                answer = len(temp_s)
            temp_s = temp_s[temp_s.index(s[i]) + 1:]
        return answer

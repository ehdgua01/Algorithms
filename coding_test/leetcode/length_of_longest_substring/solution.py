class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        temp_s = ""

        for x in s:
            if x in temp_s:
                temp_s = temp_s[temp_s.index(x) + 1 :]
            temp_s += x
            answer = answer if len(temp_s) < answer else len(temp_s)
        return answer

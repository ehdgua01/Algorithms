from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for s in zip(*strs):
            if len(set(s)) != 1:
                break
            i += 1
        return strs[0][:i]

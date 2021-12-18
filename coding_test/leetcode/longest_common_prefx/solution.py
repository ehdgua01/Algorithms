from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs[0]:
            return ""
        prefix = strs[0][0]
        while True:
            if not all(s.startswith(prefix) for s in strs):
                return prefix[:-1]
            if len(prefix) == len(strs[0]):
                return prefix
            prefix += strs[0][len(prefix)]

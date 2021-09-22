# 14 | Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        prefixes = [strs[0][:i] for i in range(len(strs[0]), 0, -1)]
        for prefix in prefixes:
            match = [str for str in strs if str[:len(prefix)] == prefix]
            if len(match) == len(strs):
                return prefix
        return ""


sol = Solution()
strs = ["flower", "flow", "flight"]
print(sol.longestCommonPrefix(strs))
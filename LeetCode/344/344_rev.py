# 344 | Reverse String
# https://leetcode.com/problems/binary-tree-postorder-traversal/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        while i < (len(s) // 2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
            i += 1
        print(s)


s = ["h","e","l","l","o"]
sol = Solution()
sol.reverseString(s)
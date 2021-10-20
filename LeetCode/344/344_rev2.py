# 344 | Reverse String
# https://leetcode.com/problems/binary-tree-postorder-traversal/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        print(s)


s = ["h","e","l","l","o"]
sol = Solution()
sol.reverseString(s)
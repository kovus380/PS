# 344 | Reverse String
# https://leetcode.com/problems/binary-tree-postorder-traversal/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right =  0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)


s = ["h","e","l","l","o"]
sol = Solution()
sol.reverseString(s)
# 125 | Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
import collections
from typing import Deque


class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True



sol = Solution()
s = "A man, a plan, a canal: Panama"
res = sol.isPalindrome(s)
print(res)
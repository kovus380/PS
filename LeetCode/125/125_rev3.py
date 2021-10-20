# 125 | Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
import re


class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


sol = Solution()
s = "A man, a plan, a canal: Panama"
res = sol.isPalindrome(s)
print(res)
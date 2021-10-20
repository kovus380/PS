# 125 | Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        stack = []
        s = s.lower()
        for i in s:
            if i.isalnum():
                stack.append(i)
        return stack == stack[::-1]


sol = Solution()
s = "0P"
res = sol.isPalindrome(s)
print(res)
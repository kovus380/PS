# 13 | Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        s = list(s)
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        while s:
            if len(s) > 1 and roman_dict[s[-1]] > roman_dict[s[-2]]:
                sum += roman_dict[s.pop()] - roman_dict[s.pop()]
            else:
                sum += roman_dict[s.pop()]
        return sum


s = "IX"
sol = Solution()
print(sol.romanToInt(s))
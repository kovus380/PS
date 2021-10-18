# 17298 | 오큰수
# https://www.acmicpc.net/problem/17298
import sys
from typing import List


def solution(n: int, a: str) -> List[int]:
    nums = list(map(int, a.split()))
    answer = [-1] * n
    stack = []

    stack.append(0)
    for i in range(1, n):
        while stack and nums[i] > nums[stack[-1]]:
            answer[stack.pop()] = nums[i]
        stack.append(i)

    return answer


n = int(input())
a = input()
res = solution(n, a)
print(*res)
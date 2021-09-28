# 86491 | 최소직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491?language=python3
from typing import List


def solution(sizes: List[int]) -> int:
    max_len = [max(size) for size in sizes]
    min_len = [min(size) for size in sizes]
    return max(max_len) * max(min_len)


sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
res = solution(sizes)
print(res)
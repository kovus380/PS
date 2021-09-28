# 68644 | 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3
from typing import List


def solution(numbers: List[int]) -> List[int]:
    answer = []
    for idx1 in range(len(numbers)):
        for idx2 in range(idx1 + 1, len(numbers)):
            answer.append(numbers[idx1] + numbers[idx2])
    return sorted(set(answer))


numbers = [5,0,2,7]
res = solution(numbers)
print(res)
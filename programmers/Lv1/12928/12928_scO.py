# 12928 | 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3
from math import sqrt


def solution(n):
    answer = set()
    for div in range(1, int(sqrt(n)) + 1):
        if n % div == 0:
            answer.add(div)
            answer.add(n//div)
    return sum(answer)


n = 100
print(solution(n))
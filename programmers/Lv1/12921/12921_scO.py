# 12921 | 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3
def prime(m: int) -> int:
    if m == 1:
        return 0
    for div in range(2, int(m**(1/2)) + 1):
        if m % div == 0:
            return 0
    return 1


def solution(n: int) -> int:
    answer = []
    for num in range(1, n + 1):
        answer.append(prime(num))
    return sum(answer)


n = 5
res = solution(n)
print(res)

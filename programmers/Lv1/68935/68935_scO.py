# 68935 | 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3
def to_10_3(n):
    if n < 3:
        return str(n)
    else:
        return str(n % 3) + to_10_3(int(n//3))


def solution(n):
    a = list(to_10_3(n)[::-1])
    answer = [int(i) * (3**idx) for idx, i in enumerate(a)]
    return sum(answer)


print(solution(45))
# 62048 | 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3
def gcd(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
    return a


def solution(w: int, h: int) -> int:
    gcd_res = gcd(w, h)
    if gcd_res == 1:
        return w * h - (w + h -1)
    else:
        return w * h - (((w // gcd_res) + (h // gcd_res) - 1) * gcd_res)


w = 8
h = 12
res = solution(w, h)
print(res)
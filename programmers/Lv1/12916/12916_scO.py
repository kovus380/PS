# 12916 | 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3
def solution(s: str) -> bool:
    s = list(s)
    return (s.count('p') + s.count('P')) == (s.count('y') + s.count('Y'))


s = "Pyy"
res = solution(s)
print(res)
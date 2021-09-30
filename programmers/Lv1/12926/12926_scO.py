# 12926 | 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3
def solution(s: str, n: int) -> str:
    answer = ''
    for ch in s:
        if ch.isupper():
            ch = chr(ord('A') + ((ord(ch) + n) % ord('A') % 26))
        elif ch.islower():
            ch = chr(ord('a') + ((ord(ch) + n) % ord('a') % 26))
        answer += ch
    return answer


s = "z"
n = 1
res = solution(s, n)
print(res)
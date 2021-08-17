

# 6550 | 부분 문자열
# https://www.acmicpc.net/problem/6550


import sys

while True:
    s = sys.stdin.readline().strip()
    if not s:
        break

    T, S = s.split()
    tag = True
    pos = 0
    for i in range(len(T)):
        found_pos = S[pos:].find(T[i])
        if found_pos < 0:
            tag = False
            break
        else:
            pos += found_pos + 1
    print("YES" if tag else "NO")

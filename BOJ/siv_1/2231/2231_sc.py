# 2231 | 분해합
# https://www.acmicpc.net/problem/2231
N = int(input())

tag = False

for i in range(1, N+1):
    if i + sum(map(int, list(str(i)))) == N:
        print(i)
        tag = True
        break

if not tag:
    print(0)

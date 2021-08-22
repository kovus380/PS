# 2839 | 설탕배달
# https://www.acmicpc.net/problem/2839
N = int(input())
N = int(input())

ex = False

for i in range(N // 3 + 1):
    for j in range(N // 5 + 1):
        if N == 3 * i + 5 * j:
            ex = True
            print(i + j)
            break
    if ex:
        break

if not ex:
    print(-1)
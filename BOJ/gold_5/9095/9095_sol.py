# 9095 | 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

def go(num):
    print(num)
    if num < 0:
        return 0
    elif num <= 1:
        return 1
    return go(num-1) + go(num-2) + go(num-3)

n = int(input())
for _ in range(n):
    print(go(int(input())))
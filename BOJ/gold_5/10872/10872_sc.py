# 10872 | 팩토리얼
# https://www.acmicpc.net/problem/10872

def factorial(m):
    if m == 1 or m == 0:
        return 1
    else:
        return m * factorial(m-1)

n = int(input())
print(factorial(n))
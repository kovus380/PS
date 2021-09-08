# 10870 | 피보나치 수 5
# https://www.acmicpc.net/problem/10870
def fibo(m):
    if m == 2 or m == 1:
        return 1

    elif m == 0:
        return 0

    else:
        return fibo(m-1) + fibo(m-2)


n = int(input())
print((fibo(n)))

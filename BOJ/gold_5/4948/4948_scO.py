# 4948 | 베르트랑 공준
# https://www.acmicpc.net/problem/4948
def find_frime(n):
    sieve = [True] * (2 * n + 1)
    for i in range(2, int((2 * n) ** 0.5) + 1):
        if sieve[i] == True:
            for j in range(2 * i, 2 * n + 1, i):
                sieve[j] = False
    return sum(sieve[n + 1:2*n + 1])


while True:
    a = int(input())
    if a == 0:
        break
    print(find_frime(a))

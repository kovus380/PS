# 에라토스테네스의 체
def prime_num(m :int) -> int:
    sieve = [True] * m
    for i in range(2, int(m ** 0.5) + 1):
        if sieve[i] == True:
            for j in range(i + i, m, i):
                sieve[j] = False
    return sum(sieve) - 2 if m > 2 else 1


def solution(n: int) -> int:
    return prime_num(n)


n = 2
res = solution(n)
print(res)
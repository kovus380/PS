

# 14490 | 백대열
# https://www.acmicpc.net/problem/14490


n, m = map(int, input().split(':'))

num = 0
for i in range(1, max(n, m)//2+1):
    if n % i == 0 and m % i == 0:
        num = i

print(n//num, ":", m//num, sep='')

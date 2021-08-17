

# 5525 | IOIOI
# https://www.acmicpc.net/problem/5525

N = int(input())
n = "I" + "OI"*N

m = int(input())
s = input()

answer = 0

for i in range(m-len(n)+1):
    if s[i:i+len(n)] == n:
        answer += 1

print(answer)
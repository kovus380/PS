

# 1357 | 뒤집힌 덧셈
# https://www.acmicpc.net/problem/1357

x, y = input().split()
x = int(x[::-1])
y = int(y[::-1])
print(int((str(x+y))[::-1]))
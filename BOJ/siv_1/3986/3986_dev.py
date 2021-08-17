

# 3986 | 좋은 단어
# https://www.acmicpc.net/problem/3986


N = int(input())
answer = 0


for i in range(N):
    word = list(input())
    stack = []
    for alpha in word:
        if not stack:
            stack.append(alpha)
        else:
            if stack[-1] == alpha:
                stack.pop()
            else:
                stack.append(alpha)
    if not stack:
        answer += 1

print(answer)

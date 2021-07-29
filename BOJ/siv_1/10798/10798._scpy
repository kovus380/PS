

# 10798 | 세로읽기
# https://www.acmicpc.net/problem/10798


from collections import deque
import sys


word = deque()
count = []
for _ in range(5):
    word.append(deque(input()))
    count.append(len(word[-1]))

for _ in range(max(count)):
    for i in range(5):
        if len(word[i]) != 0:
            print(word[i].popleft(), end='')

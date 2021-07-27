

# 17413 | 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413


from collections import deque

sen = list(input())

deque1 = deque(sen)

rev_ = []

while deque1:
    tag = []
    if deque1[0] == '<':
        rev_.reverse()
        print(''.join(rev_), end='')
        rev_ = []
        while True:
            tag.append(deque1.popleft())
            if tag[-1] == '>':
                break
        print(''.join(tag), end='')

    elif deque1[0] == ' ':
        rev_.reverse()
        rev_.append(deque1.popleft())
        print(''.join(rev_), end='')
        rev_ = []

    else:
        rev_.append(deque1.popleft())

rev_.reverse()
print(''.join(rev_), end='')


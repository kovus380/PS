

# 1543 | 문서 검색
# https://www.acmicpc.net/problem/1543


doc = input()
word = input()

answer = 0

while word in doc:
    doc = doc[doc.find(word) + len(word):]
    answer += 1

print(answer)
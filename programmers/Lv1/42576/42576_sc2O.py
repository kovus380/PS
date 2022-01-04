# 42576 | 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
from collections import Counter


def solution(participant, completion):
    counter = Counter(participant)
    for comp in completion:
        counter[comp] -= 1
    answer = [per for per in counter if counter[per]==1]
    return answer[0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
res = solution(participant, completion)
print(res)
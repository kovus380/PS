# 42576 | 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
from collections import Counter


def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
res = solution(participant, completion)
print(res)
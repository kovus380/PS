# 42578 | 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict


def solution(clothes):
    clothes_dict = defaultdict(list)

    for sample, category in clothes:
        clothes_dict[category].append(sample)

    cases = 1
    for value in clothes_dict.values():
        cases *= len(value) + 1

    return cases - 1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
res = solution(clothes)
print(res)
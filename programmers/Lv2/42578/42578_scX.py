# 42578 | 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict


def solution(clothes):
    answer = 0
    dict = defaultdict(int)
    for cloth, kind in clothes:
        dict[kind] += 1
    print(dict)
    cnts = list(dict.values())
    max_value = max(cnts)
    final_cnts = 0
    for i in range(1, max_value + 1):
        temp_cnts = 1
        for cnt in cnts:
            if cnt >= i:
                temp_cnts *= cnt
            else:
                temp_cnts *= cnt
        print(temp_cnts)
        final_cnts += temp_cnts

    return final_cnts


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
res = solution(clothes)
print(res)
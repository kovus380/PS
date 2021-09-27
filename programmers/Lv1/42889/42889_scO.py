# 42889 | 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
from typing import List


def solution(N: int, stages: List[int]) -> List[int]:
    tmp_len = len(stages)
    stage_dict = {}
    for n in range(1, N+1):
        if tmp_len == 0:
            stage_dict[n] = 0
        else:
            stage_dict[n] = stages.count(n) / tmp_len
            tmp_len -= stages.count(n)
    x = sorted(stage_dict.items(), key=lambda x:x[1], reverse=True)
    answer = [stage[0] for stage in x]
    return answer


N = 4
stages = [4,4,4,4,4]
res = solution(N, stages)
print(res)
# 42576 | 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
def solution(participant, completion):
    answer = []
    for com in completion:
        del participant[participant.index(com)]
    return participant[0]

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = 	["josipa", "filipa", "marina", "nikola"]
res = solution(participant, completion)
print(res)
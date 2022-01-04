# 42576 | 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        print(dic)
        temp += int(hash(part))
        print(temp)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
res = solution(participant, completion)
print(res)
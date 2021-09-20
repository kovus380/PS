# https://programmers.co.kr/skill_checks/311441?challenge_id=2577

def solution(number, k):
    k = len(number)-k
    answer = ''
    index = 0
    while len(answer) < k:
        # print(index, number[index:len(number)-(k-len(answer)) + 1])
        answer += max(number[index:len(number)-(k-len(answer)) + 1])
        idx = number.find(answer[-1], index)
        index = idx + 1
    return answer

print(solution("4177252841", 4))

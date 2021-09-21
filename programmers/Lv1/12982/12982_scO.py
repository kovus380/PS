# 12982 | 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3
def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(1, len(d) + 1):
        if sum(d[:i]) > budget:
            break
        else:
            answer = i
    return answer


d = [2,2,3,3]
budget = 10
print(solution(d, budget))
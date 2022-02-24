# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
def solution(numbers, target):
    answer = 0
    leaves = [0]

    for number in numbers:
        temp = []
        for parent in leaves:
            temp.extend([parent + number, parent - number])
        leaves = temp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer


numbers = [4, 1, 2, 1]
target = 4
res = solution(numbers, target)
print(res)
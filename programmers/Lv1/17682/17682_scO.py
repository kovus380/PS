# 17682 | [1차] 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3
import re
def solution(dartResult):
    answer = []
    sdt = {'S': 1, 'D': 2, 'T': 3}
    nums = list(map(int, ' '.join(re.split('[SDT*#]', dartResult)).split()))
    nums_string = [str(i) for i in range(0, 11)]
    areas = ' '.join(re.split('[0-9*#]', dartResult)).split()
    while dartResult:
        if len(dartResult) >= 2 and dartResult[:2] in nums_string:
            answer.append(int(dartResult[:2]))
            dartResult = dartResult[2:]
        elif dartResult[0] in nums_string:
            answer.append(int(dartResult[:1]))
            dartResult = dartResult[1:]
        elif dartResult[0] in sdt:
            answer[-1] = answer[-1] ** sdt[dartResult[0]]
            dartResult = dartResult[1:]
        elif dartResult[0] == '*':
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
            dartResult = dartResult[1:]
        elif dartResult[0] == '#':
            answer[-1] *= -1
            dartResult = dartResult[1:]

    temp = 0
    return sum(answer)


dartResult =	'1S*2T*3S'
res = solution(dartResult)
print(res)

def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'k')
    point = ['10' if i == 'k' else i for i in dartResult]
    sdt = ['S', 'D', 'T']

    i = -1
    for j in point:
        if j in sdt:
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0:
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)


dartResult = '1D2S#10S'
res = solution(dartResult)
print(res)

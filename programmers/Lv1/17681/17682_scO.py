# 17681 | [1차] 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
def reculsive_2(n):
    if n < 2:
        return str(n)
    return str(n % 2) + reculsive_2(n // 2)


def solution(n, arr1, arr2):
    answer = ['0'* n] * n
    for i in range(n):
        res_1 = reculsive_2(arr1[i])[::-1]
        res_2 = reculsive_2(arr2[i])[::-1]

        answer[i] = str(int(answer[i]) + int(res_1) + int(res_2))
        answer[i] = '0' * (n - len(answer[i])) + answer[i]
    answer = [''.join(' ' if elm == '0' else '#' for elm in row) for row in answer]
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
res = solution(n, arr1, arr2)
print(res)

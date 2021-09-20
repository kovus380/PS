# 12906 | 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3
def solution(arr):
    answer = []
    for num in arr:
        # using slice [-1] -> if list empty -> error
        # [-1:] -> if list empty -> not error
        # list compare, [num] not num
        if answer[-1] != [num]:
            answer.append(num)
    return answer


arr = [4, 4, 4, 3, 3]
print(solution(arr))
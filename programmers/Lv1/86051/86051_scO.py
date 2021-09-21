# 86051 | 없는 숫자 더하기
# https://programmers.co.kr/learn/courses/30/lessons/86051?language=python3
def solution(numbers):
    answer = sum(set(i for i in range(10)) - set(numbers))
    return answer


numbers = [5,8,4,0,6,7,9]
print(solution(numbers))
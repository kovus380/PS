# 12901 | 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3
def solution(a: int, b:int) -> str:
    days = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT'}
    dates = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = days[(sum(dates[:a]) + b + 4) % 7]
    return answer


a, b = 5, 24
res = solution(a, b)
print(res)
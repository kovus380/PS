# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
def solution(progresses, speeds):
    work_days = [(100 - progress) // speed + ((100 - progress) % speed != 0) for progress, speed in zip(progresses, speeds)]
    work_days.reverse()
    deploy = []
    while work_days:
        days = []
        tmp = work_days.pop()
        while work_days and work_days[-1] <= tmp:
            days.append(work_days.pop())
        days.append(tmp)
        deploy.append(len(days))
    return deploy


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
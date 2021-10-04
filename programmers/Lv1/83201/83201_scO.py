# 83201 | 상호 평가
# https://programmers.co.kr/learn/courses/30/lessons/83201?language=python3#
def solution(scores):
    answer = ''
    grade_dict = {9: 'A', 8: 'B', 7: 'C', 6: 'D', 5: 'D'}
    get_scores = [[score[i] for score in scores] for i in range(len(scores))]
    for idx, get_score in enumerate(get_scores):
        if (((min(get_score) == get_score[idx]) and (get_score.count((min(get_score))) == 1 ))) \
                or (((max(get_score) == get_score[idx])) and get_score.count((max(get_score))) == 1):
            grade = (sum(get_score) - get_score[idx]) / (len(scores) - 1) // 10
        else:
            grade = sum(get_score) / len(scores) // 10
        if grade in grade_dict:
            answer += grade_dict[grade]
        else:
            answer += 'F'
    return answer


scores = [[90, 90, 90, 90], [70, 70, 70, 70], [90, 90, 90, 90], [70, 70, 70, 70]]
res = solution(scores)
print(res)
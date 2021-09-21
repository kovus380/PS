# 42888 | 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
def solution(record):
    answer = []
    dict_id = {}
    act = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for rec in record:
        rec_split = rec.split()
        if rec_split[0] != 'Leave':
            dict_id[rec_split[1]] = rec_split[2]

    for rec in record:
        rec_split = rec.split()
        if rec_split[0] != 'Change':
            answer.append(f'{dict_id[rec_split[1]]}{act[rec_split[0]]}')
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
# https://programmers.co.kr/skill_checks/328998?challenge_id=7420
def solution(info, query):
    answer = []

    info_split = [person.split() for person in info]
    for con in query:
        con = con.split()
        tmp = [person for person in info_split if
               (person[0] == con[0] or con[0] == '-') and (person[1] == con[2] or con[2] == '-')
               and (person[2] == con[4] or con[4] == '-') and (person[3] == con[6] or con[6] == '-') and (
                       int(person[4]) >= int(con[7]))]
        answer.append(len(tmp))
    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
res = solution(info, query)
print(res)

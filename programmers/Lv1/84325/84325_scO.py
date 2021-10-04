# 84325 | 직업군 추천하기
# https://programmers.co.kr/learn/courses/30/lessons/84325?language=python3
def solution(table, languages, preference):
    scores = []
    lan_pref = dict(zip(languages, preference))
    table.sort()
    for row in table:
        score = 0
        for idx, language in enumerate(row.split()):
            if language in lan_pref:
                score += (5 - idx + 1) * lan_pref[language]
        scores.append(score)
    answer = max(scores)
    return table[scores.index(answer)].split()[0]


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
         "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
         "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

res = solution(table, languages, preference)
print(res)
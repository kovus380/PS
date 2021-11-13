# 60057 | 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
from math import sqrt


def solution(s):
    lens = []
    for unit in range(1, len(s) + 1):
        words = [s[i : i + unit] for i in range(0, len(s), unit)]
        tmp = []
        for word in words:
            if tmp[-1:] == [word]:
                tmp[-2] = str(int(tmp[-2]) + 1)
            else:
                tmp.append("1")
                tmp.append(word)
        tmp_s = ''.join(i for i in tmp if not i == "1")
        lens.append(len(tmp_s))

    return min(lens)


s = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz"
print(solution(s))
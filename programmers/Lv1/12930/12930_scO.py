# 12930 | 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3
def solution(s):
    words = s.split(' ')
    answer = []
    for word in words:
        word_upper = ''
        for idx, alpha in enumerate(word):
            if idx % 2 == 0:
                alpha = alpha.upper()
            else:
                alpha = alpha.lower()
            word_upper += alpha
        answer.append(word_upper)
    return ' '.join(answer)


s = "try            hello world strys"
print(solution(s))

#  --> "TrY HeLlO WoRlD StRyS"
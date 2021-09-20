# 81301 | 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3
def solution(s):
    answer = ''
    num_to_word = ['zero', 'one', 'two', 'three', 'four', 'five',
                   'six', 'seven', 'eight', 'nine']
    while s:
        if s[0].isdigit():
            answer += s[0]
            s = s[1:]
        else:
            for alpha_num in range(1, len(s)+1):
                if s[:alpha_num] in num_to_word:
                    answer += str(num_to_word.index(s[:alpha_num]))
                    s = s[alpha_num:]
                    break
    return answer


s = "123"
print(solution(s))

# 81301 | 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3
def solution(s):
    answer = s
    word_to_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3',
                    'four': '4', 'five': '5', 'six': '6',
                    'seven': '7', 'eight': '8', 'nine': '9'}
    for key, value in word_to_dict.items():
        answer = answer.replace(key, value)
    return answer


s = "2three45sixseven"
print(solution(s))

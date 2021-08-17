

# 15904 | UCPC는 무엇의 약자일까?
# https://www.acmicpc.net/problem/15904

def UCPC(sen):
    for i in 'UCPC':
        if i in sen:
            sen = sen[sen.index(i):]
        else:
            return "I hate UCPC"
    return "I love UCPC"

sen = input()
print(UCPC(sen))


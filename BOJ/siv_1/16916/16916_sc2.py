

# 16916 | 부분 문자열
# https://www.acmicpc.net/problem/16916


def numMatchingSubseq(S:str, P:str) -> int:

    for j in range(len(S)):
        pos = S[j:].find(P[0])
        if pos < 0:
            return 0
        elif pos > len(S) - len(P):
            return 0
        else:
            tag = True
            for i in range(1, len(P)):
                if S[j:][pos+i] != P[i]:
                    tag = False
                    break
            if tag:
                return 1
    return 0


S = input()
P = input()
print(int(numMatchingSubseq(S, P)))
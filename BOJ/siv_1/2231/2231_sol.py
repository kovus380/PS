N: int = int(input())

tag: bool = False

# 각 자리에서 가질 수 있는 가장 큰 값은 9
# 수 + 수의 각 자리 합 = 분해합이므로
# 가장 작은 수(범위를 지정할)는 분해합 - 수의 각 자리 합의 최대값
# 즉 N-9*6
for i in range(max(1, N-54), N+1):
    if i + sum(map(int, list(str(i)))) == N:
        print(i)
        tag = True
        break
    # i == N
    # -> 끝까지 갔다는 것, 즉 분해합이 존재하지 않음
    elif i == N:
        print(0)
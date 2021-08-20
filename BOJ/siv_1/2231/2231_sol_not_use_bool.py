N: int = int(input())

tag: bool = False

for i in range(1, N+1):
    if i + sum(map(int, list(str(i)))) == N:
        print(i)
        tag = True
        break
    # i == N
    # -> 끝까지 갔다는 것, 즉 분해합이 존재하지 않음
    elif i == N:
        print(0)
# 3009 | 네 번째 점
# https://www.acmicpc.net/problem/3009
x_points = []
y_points = []

for _ in range(3):
    x, y = map(int, input().split())
    if x in x_points:
        x_points.remove(x)
    else:
        x_points.append(x)

    if y in y_points:
        y_points.remove(y)
    else:
        y_points.append(y)

print(*x_points, *y_points)
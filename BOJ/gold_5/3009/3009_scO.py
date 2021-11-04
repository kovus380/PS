# 3009 | 네 번째 점
# https://www.acmicpc.net/problem/3009
x_points = []
y_points = []
for _ in range(3):
    points = input().split()
    x_points.append(points[0])
    y_points.append(points[1])
x = [point for point in x_points if x_points.count(point) == 1]
y = [point for point in y_points if y_points.count(point) == 1]
print(x[0], y[0])
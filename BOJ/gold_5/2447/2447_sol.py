# 별 찍기 - 10 | 2447
# https://www.acmicpc.net/problem/2447
def fill_star(size, x, y):
    if size == 1:
        stars[y][x] = '*'
    else:
        next_size = size // 3
        print("=" * 20)
        for dy in range(3):
            for dx in range(3):
                if not (dy == 1 and dx == 1):
                    print(next_size, x + dx * next_size, y + dy * next_size)
                    fill_star(next_size, x + dx * next_size, y + dy * next_size)


N = int(input())
stars = [[' ' for _ in range(N)] for _ in range(N)]

fill_star(N, 0, 0)
for k in stars:
    print(''.join(k))

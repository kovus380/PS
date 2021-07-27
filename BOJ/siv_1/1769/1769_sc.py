

# 1769 | 3의 배수
# https://www.acmicpc.net/submit/1769


n = input()

count = 0

while len(n) > 1:
    temp = 0
    for i in n:
        temp += int(i)
    n = str(temp)
    count += 1

print(count)
print('YES' if n in ('3', '6', '9') else 'NO')
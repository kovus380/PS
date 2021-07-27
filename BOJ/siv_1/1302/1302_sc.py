

# 1302 | 베스트셀러
# https://www.acmicpc.net/problem/1302


book_title = []
book_count = []

for _ in range(int(input())):
    title = input()
    if title in book_title:
        book_count[book_title.index(title)] += 1
    else:
        book_title.append(title)
        book_count.append(1)

win = []
value_max = max(book_count)
for idx, v in enumerate(book_count):
    if v == value_max:
        win.append(book_title[idx])

win.sort()
print(win[0])
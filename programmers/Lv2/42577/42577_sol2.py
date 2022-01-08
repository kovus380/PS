# 42577 | 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

phone_book = ["12","123","1235","567","88"]
res = solution(phone_book)
print(res)
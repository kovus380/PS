# 42577 | 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx in range(len(phone_book) - 1):
        if phone_book[idx + 1][:len(phone_book[idx])] == phone_book[idx]:
            return False
    return answer


phone_book = ["12","123","1235","567","88"]
res = solution(phone_book)
print(res)
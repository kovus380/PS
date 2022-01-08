# 42577 | 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx1, pb1 in enumerate(phone_book):
        for idx2 in range(idx1 + 1, len(phone_book)):
            if pb1 == phone_book[idx2][:len(pb1)]:
                answer = False
    return answer


phone_book = ["12","123","1235","567","88"]
res = solution(phone_book)
print(res)
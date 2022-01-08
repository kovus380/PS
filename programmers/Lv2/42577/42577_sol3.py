# 42577 | 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True
phone_book = ["12","123","1235","567","88"]
res = solution(phone_book)
print(res)
# https://programmers.co.kr/skill_checks/328998?challenge_id=5569
def solution(s):
    s = s[2:-2]
    a = s.split('},{')
    
    nums = []
    for grp in sorted(a, key=len):
        grp_split = set(grp.split(','))
        num = list(grp_split.difference(nums))[0]
        nums.append(num)

    answer = list(map(int, nums))
    return answer


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
res = solution(s)
print(res)
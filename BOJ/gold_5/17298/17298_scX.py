# 17298 | 오큰수
# https://www.acmicpc.net/problem/17298
def solution(n: int, a: str) -> str:
    nums = list(map(int, a.split()))
    answer = []
    for idx, num in enumerate(nums):
        if idx != (len(nums)-1) and max(nums[idx + 1:]) <= nums[idx]:
            answer.append('-1')
        for com_idx in range(idx + 1, len(nums)):
            if nums[idx] < nums[com_idx]:
                answer.append(str(nums[com_idx]))
                break
    answer.append('-1')
    return answer


n = input()
a = input()
res = solution(n, a)
print(' '.join(res))
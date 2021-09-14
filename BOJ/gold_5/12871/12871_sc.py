# 12871 | 무한 문자열
# https://www.acmicpc.net/problem/12871
def gcd(a: int, b: int) -> int :
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int :
    return a * b // gcd(a, b)


a = input()
b = input()

# 최소 공배수
lcm = lcm(len(a), len(b))

if a*(lcm//len(a)) == b*(lcm//len(b)):
    print(1)
else:
    print(0)


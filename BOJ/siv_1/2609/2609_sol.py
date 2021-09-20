def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_lcm(a, b):
    # 최소공배수(lcm)는 두 수의 곱을 최대공약수(gcd)로 나눈 것
    return a * b // get_gcd(a, b)


a, b = map(int, input().split())
print(get_gcd(min(a, b), max(a, b)))
print(get_lcm(min(a, b), max(a, b)))

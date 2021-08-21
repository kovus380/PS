a, b = map(int, input().split())

if a == b:
    print(a, b)

else:
    n = b // a
    # print(n)

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ( (i**2) != n) :
                divisorsList.append(n // i)

    divisorsList.sort()

    ex = True
    for i in range(len(divisorsList)//2, len(divisorsList)):
        x, y = divisorsList[i], divisorsList[len(divisorsList) - i - 1]
        for div in range(2, int(len(divisorsList)**(1/2)) + 1):
            if x % div == 0 and y % div == 0:
                # print(i, x, len(divisorsList) - i - 1, y)
                ex = False
                break
            else:
                ex = True
        if ex:
            # print(i)
            # print(x, y)
            break
    # print(divisorsList)
    # print(len(divisorsList))
    print(y*a, x*a)
N = int(input())

bag = 0
while N >= 0:
    # If dived into 5, div and print bag
    if N % 5 == 0:
       bag += N // 5
       print(bag)
       break
    # If not dived into 5, sub 3 and add 1 bag
    N -= 3
    bag += 1
else:
    print(-1)

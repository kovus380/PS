# 4358 | 생태학
# https://www.acmicpc.net/problem/4358


import sys


tree_dict = {}
tree_total = 0

for line in sys.stdin:

    if line == '\n':
        break

    tree = line.rstrip()
    tree_total += 1

    if tree in tree_dict:
        tree_dict[tree] += 1
    elif tree not in tree_dict:
        tree_dict[tree] = 1


tree_list = sorted(tree_dict.items(), key=lambda x:x[0])

for k, v in tree_list:
    percentage = round((v/tree_total)*100, 4)
    print(k, '%.4f' %percentage)
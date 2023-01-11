for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    x = []
    for i in a:
        if len(x) == 0 or i != x[-1]: x.append(i)
        elif i == x[-1]: x.pop()
    print(x[0])

# 2
# 7
# 1 2 3 2 3 1 3
# 5
# 1 1 3 3 2
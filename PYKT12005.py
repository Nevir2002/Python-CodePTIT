for t in range(int(input())):
    n,c,d = [int(x) for x in input().split()]
    if c > d: c,d = d,c
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    # print(*a)
    # print(*a[:c])
    # print(*a[c:c+d])
    res = sum(a[:c])/c + sum(a[c:c+d])/d
    print(f'{res:.6f}')

# 2
# 2 1 1
# 1 5
# 4 2 1
# 1 4 2 3
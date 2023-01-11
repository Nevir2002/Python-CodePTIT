for t in range(int(input())):
    n = int(input())
    a = [[int(x) for x in input().split()] for i in range(n)]
    a.sort(key=lambda e:e[1])
    # print(*a)
    p = 0
    res = 1
    for i in range(n):
        if a[i][0] >= a[p][1]:
            res+=1
            p = i
    print(res)



# 1
# 10
# 39 55
# 37 74
# 0 1
# 19 25
# 65 76
# 51 52
# 19 21
# 5 94
# 46 65
# 32 40
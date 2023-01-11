for t in range(int(input())):
    n,p = [int(x) for x in input().split()]
    res = 0
    i = 1
    while p*i <= n:
        res += 1
        x = i
        while x%p == 0:
            res += 1
            x //= p
        # print(p*i,res)
        i+=1
    print(res)


# 3
# 62  7
# 76  2
# 3  5
for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    inc = [-1]*n
    dec = [-1]*n
    inc[0] = a[0]
    dec[n-1] = a[n-1]
    for i in range(1,n):
        inc[i] = max(inc[i-1],a[i])
        dec[n-i-1] = min(dec[n-i],a[n-i-1])
    inc.append(-1)
    dec.append(10**10)
    # print(*inc)
    # print(*dec)
    res = 0
    for i in range(n):
        if a[i] >= inc[i-1] and a[i] < dec[i+1]:
            res+=1
    print(res)

# 3
# 3
# 1 1 1
# 3
# 1 2 3
# 7
# 2 1 3 4 6 5 7
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if(n == 0):
        print(0)
        continue
    a.sort()
    res = 0
    dp = [[1000000000 for j in range(410)]for j in range(n)]
    for j in range(1, 405):
        dp[0][j] = dp[0][j-1]
        dp[0][j] = min(dp[0][j-1], abs(a[0]-j))
    for j in range(1, n):
        for k in range(j+1, 405):
            dp[j][k] = dp[j][k-1]
            dp[j][k] = min(dp[j][k], dp[j-1][k-1]+abs(a[j]-k))
    res = 10000000
    for j in range(1, 405):
        if j >= n:
            res = min(res, dp[n-1][j])
    print(res)
dp = []
def get_min_steps(a,y,x,m,n):
    if y == m-1 and x == n-1: return 0
    if y >= m or x >= n: return 1e10
    if dp[y][x] != -1: return dp[y][x]
    n1,n2,n3 = 1e10,1e10,1e10
    if y < m-1:
        steps = abs(a[y][x] - a[y+1][x])
        if steps > 0:
            n1 = 1+get_min_steps(a,y+steps,x,m,n)
    if y < m-1 and x < n-1:
        steps = abs(a[y][x] - a[y+1][x+1])
        if steps > 0:
            n2 = 1+get_min_steps(a,y+steps,x+steps,m,n)
    if x < n-1:
        steps = abs(a[y][x] - a[y][x+1])
        if steps > 0:
            n3 = 1+get_min_steps(a,y,x+steps,m,n)
    dp[y][x] = min(n1,n2,n3)
    return dp[y][x]    

for t in range(int(input())):
    m,n = [int(x) for x in input().split()]
    a = [[0 for i in range(n)] for j in range(m)]
    dp = [[-1 for i in range(n)] for j in range(m)]
    for i in range(m):
        a[i] = [int(x) for x in input().split()]
    res = get_min_steps(a,0,0,m,n)
    # print(*dp,sep='\n')
    print(res if res < 1e10 else -1)



# 2
# 3 3
# 2 1 2
# 1 2 4
# 1 3 2
# 3 3
# 1 2 3 
# 4 5 6 
# 7 8 9
dx = [-1,0,0,1]
dy = [0,-1,1,0]

for t in range(int(input())):
    m,n = [int(x) for x in input().split()]
    res = 2*m*n
    a = [[int(x) for x in input().split()] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if a[i][j] == 0:
                res -= 2
            else:
                res += a[i][j]*4
                for k in range(4):
                    y,x = i+dy[k],j+dx[k]
                    if x >= 0 and x < n and y >= 0 and y < m:
                        res -= min(a[i][j],a[y][x])
    print(res)

# 5
# 1 1
# 1
# 1 2
# 1 2
# 1 1
# 2
# 3 3
# 1 1 1
# 1 1 1
# 1 1 1
# 3 3
# 1 1 1
# 1 2 0
# 1 0 2
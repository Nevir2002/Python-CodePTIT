
for t in range(int(input())):
    m,n,k = [int(x) for x in input().split()]
    a = [[int(x) for x in input().split()] for i in range(m)]
    for i in range(m):
        for j in range(1,n):
            a[i][j] += a[i][j-1]
    # print()
    # for i in range(m):
    #     for j in range(n):
    #         print(a[i][j],end=' ')
    #     print()
    for i in range(1,m):
        for j in range(n):
            a[i][j] += a[i-1][j]
    # print()
    # for i in range(m):
    #     for j in range(n):
    #         print(a[i][j],end=' ')
    #     print()
    for i in range(m-k+1):
        for j in range(n-k+1):
            sum = a[i+k-1][j+k-1]
            if i > 0: sum -= a[i-1][j+k-1]
            if j > 0: sum -= a[i+k-1][j-1]
            if i > 0 and j > 0: sum += a[i-1][j-1]
                
            # print(f'({sum})',end='')
            sum //= k*k
            print(sum,end=' ')
        print()

# 2
# 4 4 3
# 2 1 0 0
# 3 2 1 1
# 4 5 2 1
# 2 2 9 0
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9
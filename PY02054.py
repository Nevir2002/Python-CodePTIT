m,n = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for i in range(m)]

if m > n:
    for i in range(m):
        if i%2 == 0 and i < 2*(m-n): continue
        print(*a[i])
elif n > m:
    for i in range(m):
        for j in range(n):
            if j%2 == 1 and j <= 2*(n-m): continue
            print(a[i][j],end=' ')
        print()
else:
    for i in range(m):
        print(*a[i])


# 6 4
# 2 8 7 6
# 6 3 2 6
# 7 2 2 8
# 9 9 9 8
# 9 6 6 3
# 7 7 4 9

# 4 6
# 2 8 7 6 4 3
# 6 3 2 6 7 2
# 7 2 2 8 9 1
# 9 9 9 8 0 7
m,n = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for i in range(m)]

mxN = 0
for i in range(m):
    for j in range(n):
       if a[i][j] >= 10 and a[i][j] == int(str(a[i][j])[::-1]) and a[i][j] > mxN: mxN = a[i][j]
res = []
for i in range(m):
    for j in range(n):
        if a[i][j] == mxN:
            res.append(f'Vi tri [{i}][{j}]')

if len(res) == 0: 
    print("NOT FOUND")
else:
    print(mxN)
    print(*res,sep='\n')

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77
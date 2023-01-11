m,n = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for i in range(m)]

n1 = min(a[0])
n2 = max(a[0])
for i in range(1,m):
    n1 = min(n1,min(a[i]))
    n2 = max(n2,max(a[i]))
x = n2-n1
res = []
for i in range(m):
    for j in range(n):
        if a[i][j] == x:
            res.append(f'Vai tri [{i}][{j}]')

if len(res) == 0: 
    print("NOT FOUND")
else:
    print(x)
    print(*res,sep='\n')

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77
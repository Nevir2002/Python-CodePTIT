from math import sqrt

def prime(n):
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3,int(sqrt(n)+1),2):
        if n%i == 0: return False
    return True

m,n = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for i in range(m)]
mxprime = 0
res = []
for i in range(m):
    for j in range(n):
        if prime(a[i][j]):
            if mxprime < a[i][j]: mxprime = a[i][j]

if mxprime == 0: 
    print("NOT FOUND")
else:
    print(mxprime)
    for i in range(m):
        for j in range(n):
            if a[i][j] == mxprime: print(f'Vi tri [{i}][{j}]')

# 6 4
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29
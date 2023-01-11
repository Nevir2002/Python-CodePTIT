from math import inf
n = int(input())
a = [int(x) for x in input().split()]
res = inf
for z in range(n):
    b = a.copy()
    v = 0
    for i in range(z):
        b[i] += v
        v-=1
    for i in range(z,n):
        b[i] += v
        v+=1
    b.sort()
    b0 = max(max(b[n//2],-v),0)
    steps = 0
    for i in range(z):
        steps += abs(b0-a[i])
        b0+=1
    for i in range(z,n):
        steps += abs(b0-a[i])
        b0-=1
    res = min(res,steps)
print(res)
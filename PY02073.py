from math import inf


for t in range(int(input())):
    n = int(input())
    x,y,z = [int(x) for x in input().split()]
    a = [0 for i in range(n+1)]
    a[1] = x
    for i in range(2,n+1):
        if i%2 == 0: a[i] = min(a[i-1]+x,a[i//2]+z)
        else: a[i] = min(a[i-1]+x,a[(i+1)//2]+y+z)
    print(a[n])

x = [0]*100
x[1] = x[2] = 1
for i in range(3,94):
    x[i] = x[i-1]+x[i-2]
for t in range(int(input())):
    a,b = (int(x) for x in input().split())
    for i in range(a,b+1): print(x[i],end=' ')
    print()

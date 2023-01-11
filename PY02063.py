irr = input()
a = [int(x) for x in input().split()]
a.sort()
# print(a)
n1 = a[0]*a[1]
n2 = a[-1]*a[-2]
res = max(n1,n1*a[2],n1*a[-1],n2,n2*a[0],n2*a[-3])
print(res)

# 6
# 5 -10 -2 1 5 2
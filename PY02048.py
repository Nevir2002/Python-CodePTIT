n,k = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])
i = 0
res = []
tmp = [a[0]]
for i in range(1,len(a)):
    if a[i] - tmp[-1] <= k:
        tmp.append(a[i])
    else:
        res.append(tmp)
        tmp = [a[i]]
if len(tmp) > 0: res.append(tmp)
# print(res)
print(len(res))

# 7 1
# 2 6 1 7 3 4 9
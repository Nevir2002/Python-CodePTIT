from math import inf


n = int(input())
a = [int(x) for x in input().split()]

res = inf
idx = 0

for i in range(n):
	tmp = 0
	for j in range(n):
		if j == i: continue
		tmp += abs(a[i]-a[j])
	if tmp < res:
		idx = i
		res = tmp
print(res,a[idx])

# 8
# 13 5 8 7 9 15 26 34
def bfs(i,a,vis):
	q = []
	q.append(i)
	vis.append(i)
	while len(q) > 0:
		x = q.pop(0)
		for z in a[x]:
			if z not in vis:
				vis.append(z)
				q.append(z)

def count(a,vis,n):
	res = 0
	for i in range(1,n+1):
		if i not in vis:
			res+=1
			bfs(i,a,vis)
	return res

for t in range(int(input())):
	n,m = [int(x) for x in input().split()]
	a = [[] for i in range(n+1)]
	vis = []
	for i in range(m):
		j,k = [int(x) for x in input().split()]
		a[j].append(k)
		a[k].append(j)
	currMax = count(a,vis,n)
	res = 0
	for i in range(1,n+1):
		vis = []
		vis.append(i)
		x = count(a,vis,n)
		if x > currMax:
			currMax = x
			res = i
	print(res)


# 2
# 5 5
# 1 2
# 1 3
# 2 3
# 3 4
# 3 5
# 5 7
# 1 2
# 1 3
# 2 3
# 2 5
# 3 4
# 3 5
# 4 5
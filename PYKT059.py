def bfs(k):
	q = []
	q.append(k)
	while len(q) > 0:
		x = q[0]
		vis[x] = True
		q.pop(0)
		for i in a[x]:
			if not vis[i]:
				q.append(i)

n,m,k = [int(x) for x in input().split()]
vis = [False for i in range(n+1)]
a = [[] for i in range(n+1)]
for i in range(m):
	x,y = [int(x) for x in input().split()]
	a[x].append(y)
	a[y].append(x)
bfs(k)
check = True
for i in range(1,n+1):
	if not vis[i]: 
		print(i)
		check = False
if check: print(0)

# 6 4 2
# 1 3
# 2 3
# 1 2
# 4 5
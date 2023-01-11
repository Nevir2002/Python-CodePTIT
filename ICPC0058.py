from collections import defaultdict


vis = []
q = []
mp = {}

def check(u,v,i):
	vis.clear()
	q.clear()
	vis.append(i)
	bfs(u)
	if v in vis: return False
	return True

def bfs(i):
	vis.append(i)
	q.append(i)
	while len(q) > 0:
		n = q.pop(0)
		for adj in mp[n]:
			if adj not in vis:
				vis.append(adj)
				q.append(adj)

for t in range(int(input())):
	mp = defaultdict(list)
	m,n,u,v = [int(x) for x in input().split()]
	for i in range(n):
		a,b = [int(x) for x in input().split()]
		mp[a].append(b)
	# print(mp)
	res = 0
	for i in range(1,m+1):
		if i == u or i == v: continue
		if check(u,v,i): res+=1
	print(res)
	
# 2
# 5 7 1 3
# 1 2
# 2 4
# 2 5
# 3 1
# 3 2
# 4 3
# 5 4
# 4 5 1 4
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4
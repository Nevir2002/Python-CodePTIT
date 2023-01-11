from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

def isCyclicUtil(i,adj,vis,st):
	vis[i] = True
	st[i] = True
	# print(i,adj[i],st)
	for j in adj[i]:
		# print(i,j)
		if not vis[j]:
			if isCyclicUtil(j,adj,vis,st): return True
		elif st[j]:
			return True
	st[i] = False
	return False

def isCyclic(adj,n):
	vis = [False for i in range(n)]
	st = [False for i in range(n)]
	for i in range(n):
		if not vis[i]:
			if isCyclicUtil(i,adj,vis,st): return True
	return False

n = int(input())
adj = []
idx = 0
names = defaultdict(lambda:-1)

for t in range(n):
	n1,op,n2 = input().split()
	if names[n1] == -1:
		names[n1] = idx
		adj.append([])
		idx += 1
	if names[n2] == -1:
		names[n2] = idx
		adj.append([])
		idx += 1
	if op == '>':
		adj[names[n1]].append(names[n2])
	else:
		adj[names[n2]].append(names[n1])
# print(idx)
# print(*adj,sep='\n')
if idx == 1: print('possible')
else: print('possible' if not isCyclic(adj,idx) else 'impossible')

# 3
# An > Binh
# Binh > Cong
# An < Cong

# 3
# An > Binh
# Binh > Cong
# An > Cong

# 6
# D > A
# A > B
# B > F
# F > C
# C > A
# A > E
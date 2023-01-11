n,m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for i in range(n)]
res = 0
vis = [[False for i in range(m)] for j in range(n)]
for i in range(n):
	for j in range(m):
		if a[i][j] == -1:
			for y in range(-1,2):
				for x in range(-1,2):
					if y+i < 0 or y+i >= n or x+j < 0 or x+j >= m: continue
					if y == 0 and x == 0: continue
					if not vis[y+i][x+j]: 
						res += a[y+i][x+j]
						vis[y+i][x+j] = True
					
print(res)
# 4 4
# 1 1 0 1
# 2 -1 4 5
# 0 0 0 0
# 1 0 2 1

# 4 4
# 1 1 0 1 
# 2 -1 4 5 
# 0 0 -1 0 
# 1 0 2 1
m,n = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

vis = [0 for i in range(n+1)]

for i in a:
    vis[i] += 1

# print(vis)
res = max(vis)
while res in vis: vis[vis.index(res)] = 0
res = max(vis)
# print(vis)
print(vis.index(res) if res > 0 else "NONE")

# 10 4
# 2 3 1 2 3 4 1 2 3 2

# 8 4
# 1 2 3 4 4 3 2 1
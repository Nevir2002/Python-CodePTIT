class DS:
    def __init__(self,n):
        self.rank = [1]*n
        self.parent = [i for i in range(n)]
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset: return
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

a = DS(10**5)
for t in range(int(input())):
    x,y,q = [int(x) for x in input().split()]
    if q == 1:
        a.union(x,y)
    else:
        print(1 if a.find(x) == a.find(y) else 0)

# 9
# 1 2 2
# 1 2 1
# 3 7 2
# 2 3 1
# 1 3 2
# 2 4 2
# 1 4 1
# 3 4 2
# 1 7 2

from itertools import combinations

a,k = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
s = list(set(x))
s.sort()
for i in list(combinations(s,k)):
    print(*i)
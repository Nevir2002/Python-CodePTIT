n = int(input())
a = [[int(x) for x in input().split()] for i in range(n)]
s1 = s2 = 0
for i in range(n):
	for j in range(n):
		if j < n-i-1: s1 += a[i][j]
		elif j > n-i-1: s2 += a[i][j]

k = int(input())
print("YES" if abs(s1-s2) <= k else "NO")
print(abs(s1-s2))
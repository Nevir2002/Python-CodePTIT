from statistics import mode

for t in range(int(input())):
	n = int(input())
	a = [int(k) for k in input().split()]
	a.sort()
	res = mode(a)
	print(res if a.count(res) > n//2 else "NO")
for t in range(int(input())):
	n = int(input())
	b = [1]*n
	a = [int(x) for x in input().split()]
	for i in range(n):
		j = i-1
		while j >= 0 and a[j] <= a[i]:
			b[i] += b[j]
			j -= b[j]
	print(*b)
from math import sqrt


def prime(n):
	if n < 2: return False
	if n == 2: return True
	if n%2 == 0: return False
	for i in range(3,int(sqrt(n))+1,2):
		if n%i == 0: return False
	return True

m,n = (int(x) for x in input().split())
a = dict(dict())
for i in range(m):
	a[i] = [int(x) for x in input().split()]
for i in range(m):
	for j in range(n):
		print(1 if prime(a[i][j]) else 0,end=' ')
	print()
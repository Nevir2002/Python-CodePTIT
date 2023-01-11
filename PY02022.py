from math import sqrt


def prime(n):
	if n < 2: return False
	if n == 2: return True
	if n%2 == 0: return False
	for i in range(3,int(sqrt(n))+1,2):
		if n%i == 0: return False
	return True

n = int(input())
vis = []
a = [int(x) for x in input().split()]
for i in range(n):
	if prime(a[i]) and a[i] not in vis:
		print(a[i], a.count(a[i]))
		vis.append(a[i])
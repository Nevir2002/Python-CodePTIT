def zz(n):
	res = 1
	while(n > 0):
		res *= n%10
		n //= 10
	return res

for t in range(int(input())):
	n = int(input())
	a = [int(x) for x in input().split()]
	for i in range(n):
		for j in range(i+1,n):
			if (zz(a[i]) > zz(a[j])) or (zz(a[i]) == zz(a[j]) and a[i] > a[j]):
				tmp = a[i]
				a[i] = a[j]
				a[j] = tmp
	print(*a)
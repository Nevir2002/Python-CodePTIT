def zz(a,n):
	x = a[0]
	for i in range(n):
		if a[i] != x:
			return x
		x+=1
	return x

n = int(input())
a = [int(x) for x in input().split()]
a.sort()
print(zz(a,n))
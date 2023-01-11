from math import sqrt

n = 8000
prime = [True]*n
for i in range(2,int(sqrt(n))):
	if(prime[i]):
		for j in range(2*i,n,i):
			prime[j] = False
n,x = (int(k) for k in input().split())
print(x,end=' ')
k = 2
for i in range(n):
	while not prime[k]: 
		k+=1
	x += k
	k+=1
	print(x,end=' ')
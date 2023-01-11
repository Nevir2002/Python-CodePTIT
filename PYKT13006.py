from math import comb
a = 3
b = 5
# a = 4
# b = 11
def calc(n):
	n1 = n
	n2 = 0
	arr = []
	while n1 >= 0:
		arr.append([2*comb(n,n2),n1,n2//2])
		n1-=2
		n2+=2
	res = 0
	for x in arr:
		res += x[0]*pow(a,x[1])*pow(b,x[2])
	return (res-1)%1000

for t in range(int(input())):
	n = int(input())
	if n > 103:
		n = n%100 + (100 if n%100 < 3 else 0)
	# print(n)
	print(f'Case #{t+1}: {calc(n):03d}')
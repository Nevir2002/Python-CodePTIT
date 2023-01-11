from array import array
from math import sqrt

n = 2*10**6
res = array('i',[0]*(n+1))
for i in range(2,int(sqrt(n))+1):
	if res[i] == 0:
		res[i] = i
		for j in range(n//i + 1): res[i*j] = i
for i in range(4,n+1): res[i] += res[i//res[i]] if res[i] else i
sum = 0
from sys import stdin
n = int(stdin.readline())
while True:
	try:
		x = int(stdin.readline())
		# print(res[x])
		sum += res[x]
	except:
		break
# for line in stdin:
# 	sum += int(line)
print(sum)
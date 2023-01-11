from itertools import combinations

n,k = [int(x) for x in input().split()]

def sout(arr,a,k):
	for i in range(k):
		print(arr[a[i]],end=' ')
	print()
		
a = sorted(input().split())
arr = []
for i in a:
	if i not in arr: arr.append(i)
n = len(arr)
a = [i for i in range(n)]
x = combinations(a,k)
for i in list(x):
	sout(arr,i,k)

# 6 2
# DONG TAY NAM BAC TAY BACfrom itertools import combinations

n,k = [int(x) for x in input().split()]

def sout(arr,a,k):
	for i in range(k):
		print(arr[a[i]],end=' ')
	print()
		
a = sorted(input().split())
arr = []
for i in a:
	if i not in arr: arr.append(i)
n = len(arr)
a = [i for i in range(n)]
x = combinations(a,k)
for i in list(x):
	sout(arr,i,k)

# 6 2
# DONG TAY NAM BAC TAY BAC
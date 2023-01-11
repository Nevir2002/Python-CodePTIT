from math import ceil


for t in range(int(input())):
	n = int(input())
	a = [int(x) for x in input().split()]
	idx = 0
	curr = a[idx]
	res = 0
	while idx < n-1:
		curr = a[idx]
		if curr <= a[idx+1]:
			while curr*2 < a[idx+1]:
				curr*=2
				# print("curr ",curr)
				res+=1
		else:
			while a[idx+1]*2 < curr:
				curr=ceil(curr/2)
				# print("curr ",curr)
				res+=1
		idx+=1
	print(res)

# 6
# 4
# 4 2 10 1
# 2
# 1 3
# 2
# 6 1
# 3
# 1 4 2
# 5
# 1 2 3 4 3
# 12
# 4 31 25 50 30 20 34 46 42 16 15 16
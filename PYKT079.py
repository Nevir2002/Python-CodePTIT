for t in range(int(input())):
	n = int(input())
	a = [int(x) for x in input().split()]
	l = min(a)
	r = max(a)
	b = [0]*1001
	res = 0
	for i in a: b[i]+=1
	for i in range(l,r+1):
		if b[i] == 0: res+=1
	print(res)

# 2
# 5
# 4 5 3 8 6
# 3
# 2 1 3
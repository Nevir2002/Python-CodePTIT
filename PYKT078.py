for t in range(int(input())):
	n,k = [int(x) for x in input().split()]
	a = [int(x) for x in input().split()]
	# print(a)
	a.insert(a.index(max(a)),k)
	# print(a)
	for i in a:
		if i < 0: print(i,end=' ')
	for i in a:
		if i >= 0: print(i,end=' ')
	print()

# 1
# 5 3
# -1 2 3 4 -1
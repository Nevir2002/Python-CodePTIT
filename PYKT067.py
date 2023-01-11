from itertools import permutations
for t in range(int(input())):
	n = int(input())
	res = list(permutations([i+1 for i in range(n)]))
	print(len(res))
	for i in range(len(res)-1,-1,-1):
		print(*res[i],sep='',end=' ')
	print()

def get(n,k):
	if n == 1: return 'A'
	if n == 2:
		if k == 1 or k == 3: return 'A'
		else: return 'B'
	if k > 2**(n-1): return get(n-1,k-2**(n-1))
	if k == 2**(n-1): return chr(ord('A')+n-1)
	if k < 2**(n-1): return get(n-1,k)

for t in range(int(input())):
	n,k = [int(x) for x in input().split()]
	print(get(n,k))

# 2
# 3 2
# 4 8
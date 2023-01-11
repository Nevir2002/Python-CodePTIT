from math import ceil, log2, pow

st = []
def gcd(a: int, b: int) -> int:
	if b == 0:
		return a
	return gcd(b, a % b)

def findGcd(ss: int, se: int, qs: int, qe: int, si: int) -> int:
	if ss > qe or se < qs:
		return 0
	if qs <= ss and qe >= se:
		return st[si]
	mid = ss + (se - ss) // 2
	return gcd(findGcd(ss, mid, qs, qe, si * 2 + 1),
			findGcd(mid + 1, se, qs, qe, si * 2 + 2))

def findRangeGcd(ss: int, se: int, arr: list, n: int) -> int:
	if ss < 0 or se > n - 1 or ss > se:
		print("invalid Arguments")
		return -1
	return findGcd(0, n - 1, ss, se, 0)

def constructST(arr: list, ss: int, se: int, si: int) -> int:
	if ss == se:
		st[si] = arr[ss]
		return st[si]
	mid = ss + (se - ss) // 2
	st[si] = gcd(constructST(arr, ss, mid, si * 2 + 1),
				constructST(arr, mid + 1, se, si * 2 + 2))
	return st[si]

def constructSegmentTree(arr: list, n: int) -> list:
	global st
 
	height = int(ceil(log2(n)))
	size = 2 * int(pow(2, height)) - 1
	st = [0] * size
	constructST(arr, 0, n - 1, 0)
	return st

def findSmallestSubarr(arr: list, n: int, k: int) -> int:
	found = False
	for i in range(n):
		if arr[i] == k:
			return 1
		if arr[i] % k == 0:
			found = True
	if found == False:
		return -1
	constructSegmentTree(arr, n)
	# print(*st)
	res = n + 1
	for i in range(n - 1):
		if arr[i] % k != 0:
			continue
		low = i + 1
		high = n - 1
		closest = 0
		while True:
			mid = low + (high - low) // 2
			gcd = findRangeGcd(i, mid, arr, n)
			if gcd > k:
				low = mid
			elif gcd == k:
				high = mid
				closest = mid
			else:
				high = mid

			if abs(high - low) <= 1:
				if findRangeGcd(i, low, arr, n) == k:
					closest = low
				elif findRangeGcd(i, high, arr, n) == k:
					closest = high
				break
		if closest != 0:
			res = min(res, closest - i + 1)

	return -1 if res == n + 1 else res

for t in range(int(input())):
	st = [] # reset segment tree
	a = []
	while len(a) < 2: a += [int(x) for x in input().split()]
	n,k = a[0],a[1]
	a.pop(0)
	a.pop(0)
	while len(a) < n: a += [int(x) for x in input().split()]
	print(findSmallestSubarr(a,n,k))

# 3
# 8 3
# 6 9 7 10 12 24 36 27
# 4 3
# 2 4 6 8
# 4 6
# 1 2 3 6
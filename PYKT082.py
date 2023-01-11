from math import ceil, floor


def conv(n):
	if n >= 39: return 9.0
	if n >= 37: return 8.5
	if n >= 35: return 8.0
	if n >= 33: return 7.5
	if n >= 30: return 7.0
	if n >= 27: return 6.5
	if n >= 23: return 6.0
	if n >= 20: return 5.5
	if n >= 16: return 5.0
	if n >= 13: return 4.5
	if n >= 10: return 4.0
	if n >= 7: return 3.5
	if n >= 5: return 3.0
	if n >= 3: return 2.5
	return 1.0

for t in range(int(input())):
	a = [float(x) for x in input().split()]
	a[0] = conv(a[0])
	a[1] = conv(a[1])
	res = sum(a)/4
	if res-int(res) >= 0.75: res = ceil(res)/1.0
	elif res-int(res) >= 0.25: res = floor(res)+0.5
	else: res = floor(res)/1.0
	print(res)

# 2
# 15 25 5.0 5.5
# 22 32 6.0 6.0
mod = 10**9+7
for t in range(int(input())):
	n,m = [int(x) for x in input().split()]
	m = bin(m).replace("0b", "")[::-1]
	# print(m)
	
	res = 0
	for i in range(len(m)):
		if m[i] == '1': res += pow(n,i)
		res %= mod
	print(res)

# 3
# 3 4
# 2 12
# 105 564
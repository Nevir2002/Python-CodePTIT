def move(a,s):
	for i in range(len(s)):
		if a[i::] + a[0:i] == s: return i
	return -1

def calc(a,n):
	arr = [0]*n
	res = 10**10
	x = len(a[0])
	for i in range(1,n):
		arr[i] = move(a[i],a[0])
		if arr[i] == -1: return -1
	for i in range(x):
		tmp = 0
		for j in range(n):
			tmp += (arr[j]+i)%x
		res = min(res,tmp)
	return res

n = int(input())
a = [input() for i in range(n)]
arr = [0]*n
print(calc(a,n))

# 4
# xzzwo
# zwoxz
# zzwox
# xzzwo

# 2
# molzv
# lzvmo

# 3
# kc
# kc
# kc

# 3
# aa
# aa
# ab
def divide(s):
	n = len(s)
	return [s[:n//2],s[n//2:]]
def rotate(s):
	sum = 0
	res = [i for i in s]
	for i in s:
		sum += ord(i)-ord('A')
	for i in range(len(res)):
		res[i] = chr(ord('A')+(ord(res[i])-ord('A')+sum)%26)
	return res
def merge(a):
	res = []
	for i in range(len(a[0])):
		res.append(chr(ord('A')+(ord(a[0][i])-ord('A')+ord(a[1][i])-ord('A'))%26))
	return res
def drm(s):
	a = divide(s)
	a[0] = rotate(a[0])
	a[1] = rotate(a[1])
	return merge(a)

for t in range(int(input())):
	s = input()
	print(*drm(s),sep='')


# 3
# EWPGAJRB
# BB
# TPQJDRJWSQXGRRIPXFMINTELHBJA
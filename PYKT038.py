def val(s):
	res = 0
	for i in range(len(s)):
		res = res*2 + int(s[i])
	return res
s = input()
while len(s)%3 != 0: s = '0' + s
# print(s)
for i in range(0,len(s),3):
	print(val(s[i:i+3]),end='')
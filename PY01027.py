def check1(s):
	for i in s: 
		if i != '6' and i != '8': return False
	return True
def check2(s):
	i = 0
	while i < len(s):
		# print(i,s[i:i+3],s[i:i+2],s[i:i+1])
		if s[i:i+3] == '688':
			i += 3
		elif s[i:i+2] == '68':
			i += 2
		elif s[i:i+1] == '6':
			i += 1
		else: break
	return i >= len(s)
def check(s):
	return check1(s) and check2(s)

print("YES" if check(input()) else "NO")
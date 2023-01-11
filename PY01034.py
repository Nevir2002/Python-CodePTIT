def prev(s):
	i = len(s)-1-1
	while i > 0 and s[i] <= s[i+1]: i-=1
	if i < 0: return [-1]
	zz = i
	tmp = s[i]
	# print(i,tmp)
	i = len(s)-1
	while i >= 0 and tmp <= s[i]: i-=1
	while s[i] == s[i-1]: i-=1
	# print(i,s[i])
	z = s[i]
	s[i] = tmp
	s[zz] = z
	if s[0] == '0': return [-1]
	return s

for t in range(int(input())):
	s = prev([i for i in input().strip()])
	print(*s,sep='')

# 2
# 34123567
# 3451234446
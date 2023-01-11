a = []

def check(s):
	cnt = 0
	for i in s:
		if i == '2': cnt+=1
	return cnt > len(s)/2

def conv(n):
	# if n == 0: return 0
	res = ''
	while n > 0:
		res = str(n%3) + res
		n //= 3
	if check(res): a.append(res)

i = 2
while len(a) <= 1000: 
	conv(i)
	i += 1

# print(*a)
for t in range(int(input())):
	print(*a[:int(input())])
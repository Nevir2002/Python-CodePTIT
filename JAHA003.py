for t in range(int(input())):
	n = input()
	sum = 0
	for i in range(0,len(n),2):	sum += int(n[i:i+1])
	for i in range(1,len(n),2):	sum -= int(n[i:i+1])
	print("YES" if sum%11 == 0 else "NO")

# 2
# 12341
# 123456789123456789
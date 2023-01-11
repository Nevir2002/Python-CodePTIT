for t in range(int(input())):
	s = input()
	a = []
	sum = 0
	for i in s:
		if i.isdigit(): sum += int(i)
		else: a.append(i)
	for i in sorted(a): print(i,end='')
	print(str(sum))

# 2
# AC2BEW3
# ACCBA10D2EW30
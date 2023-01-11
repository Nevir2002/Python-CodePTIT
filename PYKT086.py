f = open("DATA.in")
t = int(f.readline())
for x in range(t):
	n = int(f.readline())
	step = 1
	if n == 4: step = 2
	if n == 8: step = 3
	if n == 16: step = 4
	s = f.readline().strip()
	# print(n,s)
	while len(s)%step != 0: s = '0' + s
	for i in range(0,len(s),step):
		tmp = int(s[i:i+step],2)
		if tmp < 10: print(tmp,end='')
		else: print(chr(ord('A')+tmp-10),end='')
	print()
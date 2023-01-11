
import fileinput

def isInt(s):
	if len(s) > 10: return False
	if not s.isdigit(): return False
	if int(s) < -2147483648 or int(s) > 2147483647: return False
	return True

a = []
for line in fileinput.input(files='DATA.in'):
	x = line.split()
	for i in x:
		if not isInt(i):
			a.append(i)
a.sort()
print(*a)

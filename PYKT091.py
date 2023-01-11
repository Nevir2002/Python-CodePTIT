import fileinput

a = []
a.append('')
for line in fileinput.input(files='VANBAN.in'):
	x = line.split()
	for i in x:
		if i == i[::-1]:
			if len(i) > len(a[0]):
				a.clear()
				a.append(i)
			elif len(i) == len(a[0]):
				a.append(i)
b = []
for i in a:
	if i not in b:
		b.append(i)
		print(i,a.count(i))

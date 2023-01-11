import fileinput

a = []
for line in fileinput.input(files='CONTACT.in'):
	if line.strip().lower() not in a: a.append(line.strip().lower())
a.sort()
for i in a:
	print(i)
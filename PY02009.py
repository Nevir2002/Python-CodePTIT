from statistics import mode

for t in range(int(input())):
	a = []
	n = int(input())
	for i in range(n):
		a.append(int(input()))
	a.sort()
	print(mode(a))

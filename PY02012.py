n = int(input())
b = []
c = []
a = []
while len(a) < n: a += [int(x) for x in input().split()]
for i in a:
	if i%2 == 0: b.append(i)
	else: c.append(i)
b.sort()
c.sort(reverse=True)
x = y = 0
for i in a:
	if i%2 == 0: 
		print(b[x],end=' ')
		x+=1
	else:
		print(c[y],end=' ')
		y+=1

# 10
# 1 2 3 4 5 6 7 7 9 6
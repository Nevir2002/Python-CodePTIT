n = input()
res = 0
sum = 0
while len(n) > 1:
	sum = 0
	for i in n:
		if i == '-': sum -= 3
		else: sum += int(i)
	n = str(sum)
	res+=1
print(res)
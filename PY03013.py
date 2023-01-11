def countDigits(digit,n):
	if n <= 0: return 0
	cnt = 0
	i = 1
	# print(f'{digit} of {n}: ')
	while i <= (n//10 if digit == 0 else n):
		unit = i*10
		cnt += (n//unit - (1 if digit == 0 else 0))*i + min(i,max(0,n%unit-digit*i+1))
		# print(f'Unit: {unit}, cnt += {(n//unit - (1 if digit == 0 else 0))*i + min(i,max(0,n%unit-digit*i+1))}')
		i *= 10
	# print(cnt)
	return cnt

for t in range(int(input())):
	a,b = [int(x) for x in input().split()]
	for i in range(10):
		print(countDigits(i,b) - countDigits(i,a-1),end=' ')
	print()
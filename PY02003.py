n = 11000
ugly = [0] * n  # To store ugly numbers
ugly[0] = 1

i2 = i3 = i5 = 0

# Set initial multiple value
next_multiple_of_2 = 2
next_multiple_of_3 = 3
next_multiple_of_5 = 5

for l in range(1, n):

	ugly[l] = min(next_multiple_of_2,
					next_multiple_of_3, 
					next_multiple_of_5)
	if ugly[l] == next_multiple_of_2:
		i2 += 1
		next_multiple_of_2 = ugly[i2] * 2
	if ugly[l] == next_multiple_of_3:
		i3 += 1
		next_multiple_of_3 = ugly[i3] * 3
	if ugly[l] == next_multiple_of_5:
		i5 += 1
		next_multiple_of_5 = ugly[i5] * 5

def find(x):
	l = 0
	r = len(ugly)-1
	while(l <= r):
		mid = (l+r)//2
		if ugly[mid] > x:
			r = mid-1
		elif ugly[mid] < x:
			l = mid+1
		else:
			return mid
	return -1

for t in range(int(input())):
	x = int(input())
	k = find(x)
	print(k+1 if k != -1 else "Not in sequence")
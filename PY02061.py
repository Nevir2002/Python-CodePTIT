for t in range(int(input())):
	sum = 0
	a,b = (int(x) for x in input().split())
	arr = [[int(x) for x in input().split()] for i in range(a)]
	brr = [[int(x) for x in input().split()] for i in range(3)]
	for i in range(1,a-1):
		for j in range(1,b-1):
			for k in range(0,3):
				for l in range(0,3):
					sum += arr[i-1+k][j-1+l]*brr[k][l]
	print(sum)
# 2
# 4 4
# 2 1 0 0
# 3 2 1 1
# 4 3 2 1
# 2 2 1 0
# -1 -1 -1
# -1 8 -1
# -1 -1 -1
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 1 1 1
# 1 1 1
# 1 1 1
n = 10
arr = []
res = set()
while(len(arr) < 10):
	x = [int(x) for x in input().split()]
	for i in x: arr.append(i)

for i in range(n):
	res.add(arr[i]%42)
print(len(res))
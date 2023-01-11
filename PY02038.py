def cal(n):
	return n*(n-1)/2

def count(a):
	res = 0
	for i in range(len(a)):
		if a[i] == 'C': res+=1
	return res

n = int(input())
res = 0
a = [input() for i in range(n)]
for i in range(n):
	res += cal(count(a[i]))
	res += cal(count([a[j][i] for j in range(n)]))
print(int(res))
# 4
# CC..
# C..C
# .CC.
# .CC.
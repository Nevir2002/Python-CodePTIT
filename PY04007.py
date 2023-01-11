class Matrix:
	def __init__(self,n,m,a):
		self.n = n
		self.m = m
		self.a = a
	def getTranspose(self):
		b = [[0 for i in range(self.n)] for j in range(self.m)]
		for i in range(self.m):
			for j in range(self.n):
				b[i][j] = self.a[j][i]
		return Matrix(self.m,self.n,b)
	def multiply(self,b):
		c = [[0 for i in range(self.n)] for j in range(b.m)]
		for i in range(self.n):
			for j in range(b.m):
				c[i][j] = 0
				for k in range(self.m): c[i][j] += self.a[i][k]*b.a[k][j]
		return Matrix(self.n,b.m,c)
	def print(self):
		for i in range(self.n):
			print(*self.a[i])

for t in range(int(input())):
	n,m = [int(x) for x in input().split()]
	a = [[int(x) for x in input().split()] for i in range(n)]
	x = Matrix(n,m,a)
	x.multiply(x.getTranspose()).print()
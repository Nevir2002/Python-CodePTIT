class Complex:
	def __init__(self,r,i):
		self.r = r
		self.i = i
	def add(self,a):
		return Complex(self.r+a.r,self.i+a.i)
	def multiply(self,a):
		return Complex(self.r*a.r - self.i*a.i, self.r*a.i+a.r*self.i)
	def print(self):
		if self.i >= 0: 
			return f'{self.r} + {self.i}i'
		elif self.i < 0: 
			return f'{self.r} - {-self.i}i'

for t in range(int(input())):
	a,b,c,d = [int(x) for x in input().split()]
	n1 = Complex(a,b)
	n2 = Complex(c,d)
	x = n1.add(n2)
	n3 = x.multiply(n1)
	n4 = x.multiply(x)
	print(f'{n3.print()}, {n4.print()}')
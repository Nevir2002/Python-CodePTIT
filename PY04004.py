from math import gcd

class Fraction:
	def __init__(self,a,b):
		self.a = a//gcd(a,b)
		self.b = b//gcd(a,b)
	def print(self):
		print(f'{self.a}/{self.b}')
	def add(self,x):
		return Fraction(self.a*x.b+x.a*self.b,self.b*x.b)

a,b,c,d = [int(x) for x in input().split()]
n1 = Fraction(a,b)
n2 = Fraction(c,d)
n1.add(n2).print()
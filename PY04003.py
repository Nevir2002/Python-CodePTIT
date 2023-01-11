from math import gcd

class Fraction:
	def __init__(self,a,b):
		self.a = a//gcd(a,b)
		self.b = b//gcd(a,b)
	def print(self):
		print(f'{self.a}/{self.b}')
		


a,b = [int(x) for x in input().split()]
r = Fraction(a,b)
r.print()
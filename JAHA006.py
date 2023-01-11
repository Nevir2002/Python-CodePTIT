class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def dist(self,a):
		return ((self.x-a.x)**2 + (self.y-a.y)**2)**0.5
class Triangle:
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
	def area(self):
		d1 = self.a.dist(self.b)
		d2 = self.a.dist(self.c)
		d3 = self.b.dist(self.c)
		if d1 + d2 <= d3 or d1 + d3 <= d2 or d2 + d3 <= d1:
			return "INVALID"
		else:
		    return '%.4f'%(0.25*((d1+d2+d3)*(d1+d2-d3)*(-d1+d2+d3)*(d1-d2+d3))**0.5)
t = int(input())
a = []
while True:
	x = [float(x) for x in input().split()]
	for i in x: a.append(i)
	if len(a) >= t*6: break
for i in range(t):
	print(Triangle(Point(a[i*6],a[i*6+1]),Point(a[i*6+2],a[i*6+3]),Point(a[i*6+4],a[i*6+5])).area())

# 3
# 0 0 0 5 0 199
# 1 1 1 1 1 1
# 0 0 0 5 5 0
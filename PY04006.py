class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def dist(self,a):
		return ((self.x-a.x)**2+(self.y-a.y)**2)**0.5

class Triangle:
	def __init__(self,p1,p2,p3):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.a = self.p1.dist(self.p2)
		self.b = self.p1.dist(self.p3)
		self.c = self.p2.dist(self.p3)
	def print(self):
		if	self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
				print('INVALID')
		else:
			print('%.2f'%(0.25*((self.a+self.b+self.c)*(self.a+self.b-self.c)*(-self.a+self.b+self.c)*(self.a-self.b+self.c))**0.5))

t = int(input())
a = []
while True:
	x = [float(x) for x in input().split()]
	for i in x: a.append(i)
	# print(len(a))
	if len(a) >= t*6: break
for i in range(t):
	Triangle(Point(a[i*6],a[i*6+1]),Point(a[i*6+2],a[i*6+3]),Point(a[i*6+4],a[i*6+5])).print()

# 3
# 0 0 0 5 0 199 1 1 1 1 1 1 0 0 0 5 5 0
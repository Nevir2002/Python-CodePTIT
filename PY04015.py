i = 1
class KH:
	def __init__(self,name,a,b):
		global i
		self.id = f'KH{i:02d}'
		i+=1
		self.name = name
		self.diff = b-a
		self.total = 0
		if self.diff > 100: self.rate = 1.05
		elif self.diff > 50: self.rate = 1.03
		else: self.rate = 1.02
		if(self.diff > 100): 
			self.total += (self.diff-100)*200
			self.diff = 100
		if(self.diff > 50): 
			self.total += (self.diff-50)*150
			self.diff = 50
		if(self.diff > 0): 
			self.total += self.diff*100
			self.diff = 0
		self.total *= self.rate
	def print(self):
		print(f'{self.id} {self.name} {self.total:.0f}')
	
a = []
for t in range(int(input())):
	a.append(KH(input(),int(input()),int(input())))
a.sort(key=lambda e:e.total,reverse=True)
for i in a: i.print()
# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612
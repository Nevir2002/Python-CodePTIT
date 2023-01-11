from decimal import Decimal


idx = 1
class HS:
	def __init__(self,name,a):
		global idx
		self.id = f'HS{idx:02d}'
		idx+= 1
		self.name = name
		self.avg =  round((sum(a)+a[0]+a[1])/12*10+Decimal(0.01))/10
		if self.avg >= 9: self.status = 'XUAT SAC'
		elif self.avg >= 8: self.status = 'GIOI'
		elif self.avg >= 7: self.status = 'KHA'
		elif self.avg >= 5: self.status = 'TB'
		else: self.status = 'YEU'
	def print(self):
		print(f'{self.id} {self.name} {self.avg} {self.status}')

a = []
for t in range(int(input())):
	a.append(HS(input(),[Decimal(x) for x in input().split()]))
a.sort(key= lambda e:e.avg, reverse=True)
for i in a: i.print()
# 3
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
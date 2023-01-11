from datetime import datetime


class xyz:
	def __init__(self,name,city,arrive):
		self.id = self.getID(name,city)
		self.name = name
		self.city = city
		self.time = arrive
		self.speed = self.calc(arrive)
	def getID(self,s1,s2):
		a = s1.split()
		b = s2.split()
		res = ''
		for i in b:
			res += i[:1]
		for i in a:
			res += i[:1]
		return res
	def calc(self,time):
		a = [int(x) for x in time.split(':')]
		a[0] -= 6
		return round(120/((a[0]*60+a[1])/60))
	def __str__(self):
		return f'{self.id} {self.name} {self.city} {self.speed} Km/h'

a = [xyz(input().strip(),input().strip(),input().strip()) for i in range(int(input()))]
a.sort(key=lambda e:e.time)
print(*a,sep='\n')

# 3
# Tran Vu Minh
# Ha Noi
# 8:30
# Vu Ngoc Hoang
# Hoa Binh
# 8:20
# Pham Dinh Tan
# An Giang
# 8:45
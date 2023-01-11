from datetime import datetime


class xyz:
	def __init__(self,id,name,roomNum,arrive,depart,add):
		self.id = id
		self.name = name
		self.roomNum = roomNum
		self.diff = self.zz(arrive,depart)
		self.cost = self.calc()
		self.total = self.cost + add
	def zz(self,s1,s2):
		d1 = datetime.strptime(s1,"%d/%m/%Y")
		d2 = datetime.strptime(s2,"%d/%m/%Y")
		return abs((d2-d1).days+1)
	def calc(self):
		i = int(self.roomNum[:1])
		if i == 1: x = 25
		if i == 2: x = 34
		if i == 3: x = 50
		if i == 4: x = 80
		return x*self.diff
	def __str__(self):
		return f'{self.id} {self.name} {self.roomNum} {self.diff} {self.total}'

a = [xyz(f'KH{i+1:02d}',input().strip(),input().strip(),input().strip(),input().strip(),int(input())) for i in range(int(input()))]
a.sort(key=lambda e:-e.total)
print(*a,sep='\n')

# 3
# Huynh Van Thanh   
# 103 
# 05/06/2010   
# 05/06/2010   
# 15
# Le Duc Cong  
# 106 
# 08/03/2010   
# 01/05/2010   
# 220
# Tran Thi Bich Tuyen   
# 207 
# 10/04/2010   
# 21/04/2010   
# 96
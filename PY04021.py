class ZZ:
	def __init__(self,id,name,start,stop):
		self.id = id
		self.name = name
		a = start.split(':')
		b = stop.split(':')
		self.val = int(b[0])*60 + int(b[1]) - int(a[0])*60 - int(a[1])
	def __str__(self):
		return f'{self.id} {self.name} {self.val//60} gio {self.val%60} phut'

a = [ZZ(input(),input(),input(),input()) for i in range(int(input()))]
a.sort(key=lambda e:e.val,reverse=True)
print(*a,sep='\n')
# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00
class MT:
	def __init__(self,id,name,test):
		self.id = id
		self.name = name
		self.test = test
	def __str__(self):
		return f'{self.id} {self.name} {self.test}'

a = [MT(input().strip(),input().strip(),input().strip()) for i in range(int(input()))]
a.sort(key= lambda e:e.id)
print(*a,sep='\n')

# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen
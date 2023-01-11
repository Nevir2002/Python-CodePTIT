class acb:
	def __init__(self,id,name,code,m1,m2):
		self.id = id
		self.name = name
		self.code = code
		self.subject = ''
		if code[:1] == 'A': self.subject = 'TOAN'
		if code[:1] == 'B': self.subject = 'LY'
		if code[:1] == 'C': self.subject = 'HOA'
		bonus = 0
		if code[1:2] == '1': bonus = 2
		if code[1:2] == '2': bonus = 1.5
		if code[1:2] == '3': bonus = 1
		self.total = m1*2+m2 + bonus
		self.status = 'LOAI'
		if self.total >= 18: self.status = 'TRUNG TUYEN'
	def __str__(self):
		return f'{self.id} {self.name} {self.subject} {self.total:.1f} {self.status}'

a = [acb(f'GV{i+1:02d}',input().strip(),input().strip(),float(input()),float(input())) for i in range(int(input()))]
a.sort(key=lambda e:-e.total)
print(*a,sep='\n')

# 3
# Le Van Binh
# A1
# 7.0
# 3.0
# Tran Van Toan
# B3
# 4.0
# 7.0
# Hoang Thi Tam
# C2
# 7.0
# 6.0
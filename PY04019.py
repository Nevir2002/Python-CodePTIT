i = 1

class TS:
	def __init__(self,name,a,b):
		global i
		self.id = f'TS0{i}'
		i+=1
		self.name = name
		while a > 10: a/=10
		while b > 10: b/=10
		self.total = (a+b)/2
		if self.total > 9.5: self.status = "XUAT SAC"
		elif self.total >= 8: self.status = "DAT"
		elif self.total >= 5: self.status = "CAN NHAC"
		else: self.status = "TRUOT"

	def __str__(self):
		return f'{self.id} {self.name} {self.total:.2f} {self.status}'

a = [TS(input(),float(input()),float(input())) for i in range(int(input()))]
a.sort(key= lambda e:e.total,reverse=True)
print(*a,sep='\n')
# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56
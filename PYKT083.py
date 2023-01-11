from collections import defaultdict


class Fee:
	def __init__(self,a):
		self.id = a[0]
		self.type = a[1]
		self.num = int(a[2])
		self.dir = a[3]
		self.date = a[4]
		self.fee = 0
		if self.dir == 'IN':
			if self.type == 'Xe_con':
				if self.num == 5: self.fee = 10000
				if self.num == 7: self.fee = 15000
			if self.type == 'Xe_tai':
				if self.num == 2: self.fee = 20000
			if self.type == 'Xe_khach':
				if self.num == 29: self.fee = 50000
				if self.num == 45: self.fee = 70000
	
a = defaultdict(lambda:0)
for t in range(int(input())):
	x = Fee(input().split())
	a.update({x.date:a[x.date]+x.fee})

# print(*a)
for x in a.keys(): print(f'{x}: {a[x]}')

# 5
# 30F-123.15 Xe_con 5 OUT 06/11/2021
# 30F-123.15 Xe_con 5 IN 06/11/2021
# 30H-123.15 Xe_con 7 IN 06/11/2021
# 29H-222.68 Xe_tai 2 IN 07/11/2021
# 30G-511.15 Xe_con 5 IN 07/11/2021
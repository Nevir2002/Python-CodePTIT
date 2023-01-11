class zz:
	def __init__(self,id,name,quantity,cost,reduce):
		self.id = id
		self.name = name
		self.quantity = quantity
		self.cost = cost
		self.buy = quantity*cost
		self.reduce = reduce
		self.total = self.buy-reduce
	def __str__(self):
		return f'{self.id} {self.name} {self.quantity} {self.cost} {self.reduce} {self.total}'

a = [zz(input().strip(),input().strip(),int(input().strip()),int(input().strip()),int(input().strip())) for i in range(int(input()))]
a.sort(key=lambda e: -e.total)
print(*a,sep='\n')

# 3
# ML01
# May lanh SANYO
# 12
# 4000000
# 2400000
# ML02
# May lanh HITACHI
# 4
# 2550000000
# 0
# ML03
# May lanh NATIONAL
# 5
# 3000000
# 150000

n = int(input())
a = [len(input().split()) for t in range(n)]
# print(a)
res = []
cnt = 0
for i in range(n):
	if i == 0:
		if a[i] == 7:
			res.append(2)
			cnt += 1
		else: res.append(1)
	else:
		if a[i] == 7:
			if a[i-1] != 7:
				res.append(2)
				cnt = 1
			else: 
				cnt += 1
				if cnt > 4:
					res.append(2)
					cnt = 1
		if a[i] != 7 and a[i-1] == 7: res.append(1)

print(len(res))
print(*res,sep='\n')
# 12
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay
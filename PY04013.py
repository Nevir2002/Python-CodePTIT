
a = {}
id = 1
for t in range(int(input())):
	name = input()
	tmp = [int(x) for x in input().split(':')]
	start = tmp[0]*60 + tmp[1]
	tmp = [int(x) for x in input().split(':')]
	stop = tmp[0]*60 + tmp[1]
	time = stop-start
	amount = float(input())
	if name not in a.keys():
		x = 'T' + '%02d'%id
		id += 1
		a.update({name:[time,amount,x]})
	else:
		a.get(name)[0] += time
		a.get(name)[1] += amount
for x in a.keys():
	print(a.get(x)[2],x,'%.2f'%(a.get(x)[1]*60/a.get(x)[0]))
		
# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35
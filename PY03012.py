a = []
for t in range(int(input())):
	a.append((input(),input().split()))
a.sort(key = lambda e:(-int(e[1][0]),  int(e[1][1]), e[0]))
for i in a:
	print(i[0],i[1][0],i[1][1])
# 5
# Nguyen Van Nam
# 168 600
# Tran Thi Naaoc
# 168 600
# Tran Thi Naasdaoc
# 1680 600
# NBT
# 169 600
# asd
# 169 500
b = {}
def convert(s):
	res = ''
	for i in range(len(s)):
		if s[i].isalpha(): res += s[i]
		else: res += ' '
	return res
for t in range(int(input())):
	s = input()
	s = convert(s.lower()).split()
	for i in s:
		if i in b: b[i]+=1
		else: b[i] = 1
for i in sorted(b.items(), key=lambda e:(-e[1],e[0])):
	print(i[0], i[1])
# 3
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.
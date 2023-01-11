b = {}
def convert(s):
	res = ''
	for i in range(len(s)):
		if s[i].isalnum(): res += s[i]
		else: res += ' '
	return res
t,k = [int(x) for x in input().split()]
for x in range(t):
	s = input()
	s = convert(s.lower()).split()
	for i in s:
		if i in b: b[i]+=1
		else: b[i] = 1
for i in sorted(b.items(), key=lambda e:(-e[1],e[0])):
	if i[1] >= k: print(i[0], i[1])
# 3 2
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.
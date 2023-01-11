for t in range(int(input())):
	s = input()
	i = 99
	while(i > 0 and i < len(s) and s[i] != ' '): i-=1
	print(s[:min(len(s),i)])

# 2
# Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021
# Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen
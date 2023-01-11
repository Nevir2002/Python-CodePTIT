def union(s1,s2):
	a = []
	for i in s1:
		if i not in a: a.append(i)
	for i in s2:
		if i not in a: a.append(i)
	return sorted(a)

def intersection(s1,s2):
	a = []
	for i in s1:
		if i in s2 and i not in a: a.append(i)
	return sorted(a)

a = input().lower().split()
b = input().lower().split()
# print(a)
# print(b)
print(*union(a,b))
print(*intersection(a,b))

# Lap trinh huong doi tuong
# Ngon ngu lap trinh C++
s = input()
a = []
for i in range(0,len(s),2):
    x = s[i:i+2]
    if len(x) == 2: a.append(x)
a = sorted(list(set(a)))
print(*a)
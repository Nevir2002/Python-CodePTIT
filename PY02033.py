s = input()
a = []
for i in range(0,len(s),2):
    x = s[i:i+2]
    if len(x) == 2 and x not in a: a.append(x)
print(*a)
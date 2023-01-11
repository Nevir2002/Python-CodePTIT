a = []
b = []
f = open("DATA1.in",'r')
for line in f.readlines():
    for i in line.lower().split():
        if i not in a: a.append(i)
f.close()
f = open("DATA2.in",'r')
for line in f.readlines():
    for i in line.lower().split():
        if i not in b: b.append(i)
f.close()
a.sort()
b.sort()
# print(*a)
# print(*b)
for i in a:
    if i not in b:
        print(i,end=' ')
print()
for i in b:
    if i not in a:
        print(i,end=' ')
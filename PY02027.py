a = []

for t in range(int(input())):
    s = input()
    tmp = ''
    for i in s:
        if i.isdigit(): tmp += i
        else:
            if len(tmp) > 0:
                a.append(int(tmp))
                tmp = ''
    if len(tmp) > 0: a.append(int(tmp))
a.sort()
print(*a,sep='\n')

# 3
# A129h
# G07bxjq3
# aaaaaaa4aaaa
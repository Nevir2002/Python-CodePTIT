s = input()
c1 = 0
c2 = 0
for i in range(len(s)):
    if s[i].isupper():
        c1 += 1
    else:
        c2 += 1
if c2 >= c1:
    print(s.lower())
else:
    print(s.upper())
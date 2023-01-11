s = input()
res = 0
for i in range(len(s)):
    if s[i] == '4' or s[i] == '7': 
        res += 1

if res == 4 or res == 7:
    print("YES")
else:
    print("NO")
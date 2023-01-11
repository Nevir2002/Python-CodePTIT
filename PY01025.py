s = input()
res = ""
i = len(s)-1
cnt = 0
while(i >= 0):
    cnt += 1
    res += s[i]
    if(cnt == 3 and i > 0):
        cnt = 0
        res += ','
    i -= 1
print(res[::-1])
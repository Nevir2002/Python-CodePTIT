def check(s):
    if len(s) < 2: return False
    l = r = 1
    stat = "up" if s[1] > s[0] else "down"
    # print(stat)
    for i in range(1,len(s)):
        if s[i] > s[i-1] and stat == "down":
            r -= 1
            stat = "up"
        elif s[i] < s[i-1] and stat == "up":
            l -= 1
            stat = "down"
        elif s[i] == s[i-1]: return False
    # print(l,r)
    return l >= 0 and r >= 0

for t in range(int(input())):
    n = input()
    if(check(n)): print("YES")
    else: print("NO")
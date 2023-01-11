def check(s):
    if(len(s) <= 1): return False
    l = 0
    r = len(s)-1
    while(l < r):
        if s[l] != s[r]: return False
        l += 1
        r -= 1
    return True

for t in range(int(input())):
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if(check(str(sum))): print("YES")
    else: print("NO")
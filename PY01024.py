def check1(n):
    sum = 0
    while(n > 0):
        sum += n%10
        n = int(n/10)
    if(sum%10 == 0): return True
    else: return False

def check2(n):
    s = str(n)
    for i in range(len(s)-1):
        if(abs(ord(s[i])-ord(s[i+1])) != 2): return False
    return True

for t in range(int(input())):
    n = int(input())
    if(check1(n) and check2(n)): print("YES")
    else: print("NO")
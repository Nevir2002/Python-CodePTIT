def check(s):
    n = len(s)
    for i in range(0,n,2):
        if(s[i] != s[0]): return False
    for i in range(1,n,2):
        if(s[i] != s[1]): return False
    return True

for t in range(int(input())):
    n = input()
    if check(n): print("YES")
    else: print("NO")
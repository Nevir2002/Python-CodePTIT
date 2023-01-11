def check(s):
    for i in range(2,len(s),2):
        if(s[i] != s[i-2]): return False
    return True

for t in range(int(input())):
    n = input()
    if(len(n)%2 != 0 and n[0] != n[1] and check(n)): print("YES")
    else: print("NO")
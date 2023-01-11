for t in range(int(input())):
    s = input()
    n = len(s)
    if(s[n-2]+s[n-1] == "86"): print("YES")
    else: print("NO")
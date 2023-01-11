for t in range(int(input())):
    s = input()
    n = len(s)
    s1 = s[0]+s[1]
    s2 = s[n-2]+s[n-1]
    if s1 == s2:
        print("YES")
    else:
        print("NO") 
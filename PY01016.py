def check(s):
    for i in range(1,len(s)):
        if(s[i] < s[i-1]): return False
    return True

for t in range(int(input())):
    s = input()
    for i in range(0,len(s)-1,2):
        c = s[i]
        t = int(s[i+1])
        for j in range(t):
            print(c,end='')
    print()
def check(s):
    for i in range(len(s)):
        if(ord(s[i])%2 != 0): return False
    return True

def dup(n):
    return int(str(n)+str(n)[::-1])

for t in range(int(input())):
    n = int(input())
    i = 2
    while(dup(i) < n):
        if(check(str(dup(i)))): print(dup(i),end=' ')
        i+=2
    print()
    
t = int(input())

def check(s):
    n = len(s)
    for i in range(1,n-1):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[n-i-1]) - ord(s[n-i])):
            # print(i,s[i],s[i-1],s[n-i-1],s[n-i])
            return False
    
    return True

while t != 0:
    
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")

    t -= 1
    
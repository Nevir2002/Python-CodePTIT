def check(s):
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
            return False
    return True

for t in range(int(input())):
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")
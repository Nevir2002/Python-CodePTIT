flag = False

def check(s):
    if s[0] == '0' or s[3] == '/' or s[3] == '*' or s[5] == '0' or s[10] == '0': return False
    arr = ''.join(s)
    a = int(arr[:2])
    b = int(arr[5:7])
    c = int(arr[10:])
    if s[3] == '+':
        if a+b==c: return True
    if s[3] == '-':
        if a-b==c: return True
    if s[3] == '?':
        if a+b==c:
            s[3] = '+'
            return True
        if a-b==c: 
            s[3] = '-'
            return True
    return False


def gen(i,s):
    global flag
    # print(i,': ',*s,sep='')
    if flag: return
    if i > 11:
        # print(i,': ',*s,sep='')
        if check(s):
            print(*s,sep='')
            flag = True
        return
    if s[i] == '?' and i != 3:
        a = s.copy()
        for j in range(10):
            a[i] = str(j)
            gen(i+1,a)
    else:
        gen(i+1,s)

for t in range(int(input())):
    s = list(input())
    flag = False
    gen(0,list(s))
    if not flag: print("WRONG PROBLEM!")
def check(n):
    while n > 0:
        if((n%10)%2 != 0): return False
        n = int(n/10)
    return True

def dup(n):
    s1 = str(n)
    s2 = s1[::-1]
    return s1+s2

for t in range(int(input())):
    s = input()
    n = int(len(s)/2)
    m = ""
    for i in range(n): m += '9'
    for i in range(1,int(m),1):
        if check(i) and int(dup(i)) < int(s):
                print(dup(i),end=" ")
    print()

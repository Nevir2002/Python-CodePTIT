n = int(input())

def check(s):
    a = s.count('2')
    b = s.count('3')
    c = s.count('5')
    d = s.count('7')
    if not ((len(s) >= 4) and (a > 0) and (b > 0) and (c > 0) and (d > 0) and (a+b+c+d == len(s)) and (s[-1] != '2')): return False
    return True

def gen(s,n):
    if len(s) == n:
        if check(s): print(s)
    else:
        gen(s+'2',n)
        gen(s+'3',n)
        gen(s+'5',n)
        gen(s+'7',n)
for i in range(4,n+1):
    gen('',i)
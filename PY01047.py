from math import sqrt

def prime(n):
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i == 0: return False
    return True

for t in range(int(input())):
    n = input()
    x = len(n)
    b = n[x-4:x:1]
    if(prime(int(b))): print("YES")
    else: print("NO")
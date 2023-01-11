from math import sqrt

def prime(n):
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i == 0: return False
    return True
def check(n):
    a = b = 0
    for i in range(len(n)):
        if prime(int(n[i])): a += 1
        else: b += 1
    return a > b

for t in range(int(input())):
    n = input()
    if prime(len(n)) and check(n): print("YES")
    else: print("NO")
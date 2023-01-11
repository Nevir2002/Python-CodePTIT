from math import sqrt

def prime(n):
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i == 0: return False
    return True

def primeList(s):
    a = b = 0
    for i in range(len(s)):
        if(prime(int(s[i]))): a += 1
        else: b += 1
    return a > b

for t in range(int(input())):
    s = input() 
    if prime(len(s)) and primeList(s):
        print("YES")
    else:
        print("NO")

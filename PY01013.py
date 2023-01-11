import math

def sumDigit(n):
    res = 0
    while n > 0:
        res += n%10
        n = int(n/10)
    return res

def prime(n):
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3,int(math.sqrt(n)+1),2):
        if n%i == 0: return False
    return True

for t in range(int(input())):
    a,b = [int(x) for x in input().split()]
    x = math.gcd(a,b)
    if(prime(sumDigit(x))):
        print("YES")
    else:
        print("NO")

import math

def prime(n):
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3,math.sqrt(n)+1,2):
        if n%i == 0: return False
    return True

for t in range(int(input())):

    n = int(input())
    res = 0
    for i in range(n):
        if math.gcd(i,n)==1: 
            res += 1
    
    # print(res)
    if(prime(res)):
        print("YES")
    else:
        print("NO")
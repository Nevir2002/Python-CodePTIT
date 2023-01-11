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
    print("YES" if(prime(int(n[-4::]))) else "NO")
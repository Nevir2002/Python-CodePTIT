from math import sqrt


def prime(n):
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i == 0: return False
    return True
def check(s):
    for i in range(len(s)):
        if int(s[i])%2 != i%2: return False
    return True

for t in range(int(input())):
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    print("YES" if prime(sum) and check(n) else "NO")
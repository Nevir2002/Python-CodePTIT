import math

def prime(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(3,int(math.sqrt(n)+1),2):
        if n%i == 0: return False
    
    return True

def check(num):
    for i in num:
        if not prime(int(i)): return False
    return True

def sum(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum

t = int(input())
while t != 0:
    
    num = input()
    if prime(int(num)) and prime(int(num[::-1])) and prime(sum(num)) and check(num):
        print("Yes")
    else:
        print("No")

    t -= 1
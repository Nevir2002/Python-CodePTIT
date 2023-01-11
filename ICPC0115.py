import math

def check(n):
    sum = 0
    for i in n:
        sum += math.factorial(int(i))
    return sum == int(n)

t = int(input())
while t != 0:
    
    num = input()
    if check(num): print("Yes")
    else: print("No")

    t -= 1
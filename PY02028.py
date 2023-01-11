from math import sqrt


def prime(n):
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3,int(sqrt(n)+1),2):
        if n%i == 0: return False
    return True

irrelevant = input()
a = [int(x) for x in input().split()]
b = []
for i in a: 
    if prime(i): b.append(i)
b.sort()
idx = 0
for i in a:
    if prime(i):
        print(b[idx],end=' ')
        idx += 1
    else: print(i,end=' ')
# print(a)

# 8
# 4 6 3 8 7 2 5 9
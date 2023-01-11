import sys
from math import sqrt


def prime(n):
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3,int(sqrt(n)+1),2):
        if n%i == 0: return False
    return True

irrelevant = input()
k = [int(x) for x in input().split()]
a = []
for i in k:
    if i not in a: a.append(i)
s = []
s.append(a[0])
for i in range(1,len(a)):
    s.append(s[i-1]+a[i])
sum = s[-1]
# print(sum)
for i in range(len(s)):
    # print(s[i], sum-s[i])
    if prime(s[i]) and prime(sum-s[i]):
        print(i)
        sys.exit()
print("NOT FOUND")

# 10
# 3 6 7 3 4 7 3 6 4 4

# 10
# 3 6 7 3 5 7 3 6 6 7
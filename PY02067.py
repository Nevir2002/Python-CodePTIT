from math import sqrt
n = input()
a = [int(x) for x in input().split()]

def divAll(n):
    for i in a:
        x1 = i//n
        x2 = x1 + 1
        if i//x1 != n and i//x2 != n: return False
    return True

def getMin(n,k):
    return n//(k+1)+1

def factorize(n):
    res = []
    while n%2 == 0:
        n /= 2
        res.append(2)
    for i in range(3,int(sqrt(n)+1),2):
        if n%i == 0:
            n /= i
            res.append(i)
    if n > 2: res.append(n)
    return res

minNum = min(a)
# fact = factorize(minNum)
curr = minNum
while True:
    # div = getMin(minNum,curr)
    div = curr
    if divAll(div):
        sum = 0
        # print(curr,div)
        for i in a:
            x = getMin(i,div)
            sum += x
        #     print(x,end=' ')
        # print()
        print(sum)
        break
    else:
        # if len(fact) > 0:
        curr -= 1
            # fact.pop(0)
        # else: break

# 5 
# 18 27 16 22 6
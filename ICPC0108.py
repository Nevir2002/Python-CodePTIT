t = int(input())

def findTriplet(a,n):
    a.sort()
    res = 0
    for i in range(n-2):
        l = i+1
        r = n-1
        while l < r:
            if a[i] + a[l] + a[r] == 0:
                res += 1
                l += 1
                
            elif a[i] + a[l] + a[r] > 0:
                r -= 1
            else:
                l += 1
    return res

while t != 0:
    
    n = int(input())
    a = [int(a) for a in input().split()]
    print(findTriplet(a,n))

    t -= 1
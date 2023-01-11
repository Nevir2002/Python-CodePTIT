t = int(input())

while t != 0:
    
    n = [int(n) for n in input().split()]
    a = [int(a) for a in input().split()]
    for i in range(n[1],n[0]):
        print(a[i],end=' ')
    for i in range(n[1]):
        print(a[i],end=' ')
    print()

    t -= 1
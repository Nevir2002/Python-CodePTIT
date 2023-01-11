t = int(input())

def getMin(a,b,c,d):
    s1 = ""
    s2 = ""
    for i in range(len(a)):
        if a[i] == str(d):
            s1 += str(c)
        else:
            s1 += a[i]
    for i in range(len(b)):
        if b[i] == str(d):
            s2 += str(c)
        else:
            s2 += b[i]
    return int(s1) + int(s2)

def getMax(a,b,c,d):
    s1 = ""
    s2 = ""
    for i in range(len(a)):
        if a[i] == str(c):
            s1 += str(d)
        else:
            s1 += a[i]
    for i in range(len(b)):
        if b[i] == str(c):
            s2 += str(d)
        else:
            s2 += b[i]
    return int(s1) + int(s2)

while t != 0:
    
    arr = [int(arr) for arr in input().split()]
    if arr[0] > arr[1]:
        arr[0],arr[1] = arr[1],arr[0]
    try:
        x = [str(x) for x in input().split()]
        print(getMin(x[0],x[1],arr[0],arr[1]),getMax(x[0],x[1],arr[0],arr[1]))
    except:
        b = input()
        print(getMin(x[0],b,arr[0],arr[1]),getMax(x[0],b,arr[0],arr[1]))

    t -= 1
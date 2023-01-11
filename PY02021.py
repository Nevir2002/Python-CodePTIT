def uni(a,b,c):
    res = []
    x = y = z = 0
    while x < len(a) and y < len(b) and z < len(c):
        if a[x] == b[y] and b[y] == c[z]:
            res.append(a[x])
            x+=1
            y+=1
            z+=1
        elif a[x] <= b[y] and a[x] <= c[z]:
            x+=1
        elif b[y] <= a[x] and b[y] <= c[z]:
            y+=1
        elif c[z] <= a[x] and c[z] <= b[y]:
            z+=1        

    return res

for t in range(int(input())):
    irrelevant = input()
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    
    res = uni(a,b,c)
    if len(res) > 0: print(*res)
    else: print("NO")

# 3
# 6 5 8
# 1 5 10 20 40 80
# 5 7 20 80 100
# 3 4 15 20 30 70 80 120
# 3 5 4
# 1 5 5
# 3 4 5 5 10
# 5 5 10 20
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9
n = int(input())
if n == 1: print("NO")
elif n == 2: print("YES")
else:
    pv1,pv2 = [int(x) for x in input().split()]
    pv3,pv4 = [int(x) for x in input().split()]
    chk = True
    pv = 0
    if pv1 == pv3 or pv1 == pv4:
        pv = pv1
    elif pv2 == pv3 or pv2 == pv4:
        pv = pv2
    else: chk = False
    for i in range(n-3):
        a,b = [int(x) for x in input().split()]
        if a != pv and b != pv:
            chk = False

    print("Yes" if chk else "No")

# 5
# 1 2
# 1 3
# 1 4
# 1 5
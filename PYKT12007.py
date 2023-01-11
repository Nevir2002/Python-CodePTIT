def avg(a,bonus):
    return (sum(a)+bonus)/len(a)
def product(a):
    res = 1
    for i in a:
        res *= i
    return res

for t in range(int(input())):
    n = int(input())
    u = float(input())
    a = [float(x) for x in input().split()]
    b = []
    if u == 0:
        print(f'{product(a):.6f}')
        continue
    k = max(a)
    while avg(a,u) <= k:
        b.append(k)
        a.remove(k)
        k = max(a)
    # print("a:", *a)
    # print("b:", *b)
    res = pow(avg(a,u),len(a))*product(b)
    res = min(res,1)
    print(f'{res:.6f}')

# 4
# 4
# 1.4000
# 0.5000 0.7000 0.8000 0.6000
# 2
# 1.0000
# 0.0000 0.0000
# 3
# 0
# 0.1 0.5 0.5
# 3
# 0.2
# 0.5 0.8 0.6

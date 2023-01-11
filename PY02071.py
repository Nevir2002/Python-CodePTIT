res = []
def gen(q):
    q.sort(reverse=True)
    if q not in res: 
        res.append(q.copy())
    if q[0] == 1:
        return
    n = q[0]
    q.pop(0)
    for i in range(1,n//2+1):
        x = q.copy()
        x.append(i)
        x.append(n-i)
        # print(x)
        gen(x)
for t in range(int(input())):
    n = int(input())
    res = []
    q = []
    q.append(n)
    gen(q)
    res.sort(reverse=True)
    print(len(res))
    for i in res:
        print('(',end='')
        print(*i,end='')
        print(')',end=' ')
    print()
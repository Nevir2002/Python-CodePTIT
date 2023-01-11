from os import remove


n = int(input())
a = [float(x) for x in input().split()]
n1 = min(a)
n2 = max(a)
while(a.count(n1) > 0): a.remove(n1)
while(a.count(n2) > 0): a.remove(n2)

print('%.2f'%(sum(a)/len(a)))
def intersection(a,b):
    res = []
    for i in a:
        if i in b: res.append(i)

    return res

def zz(a,b):
    res = []
    for i in a:
        if i not in b: res.append(i)

    return res

irrelevant = input()
a = sorted(list(set([int(x) for x in input().split()])))
b = sorted(list(set([int(x) for x in input().split()])))
# print(a)
# print(b)
k = intersection(a,b)
print(*k)
print(*zz(a,b))
print(*zz(b,a))

# 5 6
# 1 2 3 4 5
# 3 4 5 6 7 8
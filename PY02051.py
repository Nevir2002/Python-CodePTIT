
n = int(input())
a = [[int(x) for x in input().split()] for i in range(n)]
res = [0] * n
if n == 2: 
    res[0] = 1
    res[1] = a[1][0]-1
else:
    for i in range(n-1):
        if i == 0:
            res[1] = (a[1][0] + a[2][1] - a[2][0])//2
            res[0] = a[1][0] - res[1]
        else:
            res[i+1] = a[i+1][0] - res[0]
print(*res)

# 2
# 0 2
# 2 0

# 4
# 0 3 6 7
# 3 0 5 6
# 6 5 0 9
# 7 6 9 0

# a+b = x
# a-b = y

# a = (x+y)/2
# b = (x-y)/2
# 0 1
# 0 2
# 0 3


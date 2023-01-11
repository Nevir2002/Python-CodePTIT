n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [(a[i],b[i],a[i]-b[i]) for i in range(n)]
c.sort(key=lambda e:e[2])
# print(*c)
sum = 0
i = 0
while i < k:
    sum += c[i][0]
    i += 1
while i < n and c[i][2] < 0:
    sum += c[i][0]
    i+=1
while i < n:
    sum += c[i][1]
    i += 1
print(sum)

# 3 1
# 5 4 6
# 3 1 5

# 5 4
# 3 4 7 10 3
# 4 5 5 12 5
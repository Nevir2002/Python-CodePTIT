n = int(input())
a = [int(x) for x in input().split()]
res = 0
i = 0
num = max(a)
if a[n-1] == num: res = 1
while i < n-1:
    if a[i] == num:
        currLen = 1 
        while i < n-1 and a[i+1] == num:
            i+=1
            currLen+=1
        if currLen > res: res = currLen
    i+=1
print(res)
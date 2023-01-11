n = int(input())
a = []
while len(a) < n:
    x = [int(k) for k in input().split()]
    a += x
i = 1
cnt = 0
for x in a:
    while i < x:
        print(i)
        cnt+=1
        i += 1
    i += 1
if cnt == 0: print("Excellent!")
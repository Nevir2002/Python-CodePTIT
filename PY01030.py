import math

n,k = (int(x) for x in input().split())
bot = 1
top = 10
for i in range(k-1):
    bot *= 10
    top = top*10
cnt = 0
for i in range(bot,top):
    if(math.gcd(i,n) == 1):
        cnt += 1
        print(i,end=' ')
        if(cnt%10 == 0): print()
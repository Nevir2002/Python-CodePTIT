for t in range(int(input())):
    n = int(input())
    print(1,end='')
    cnt = 0
    while(n%2 == 0):
        cnt += 1
        n /= 2
    if(cnt > 0):
        print(" * ",2,"^",cnt,sep='',end='')
    i = 3
    while(i*i <= n):
        cnt = 0
        while(n%i == 0):
            cnt += 1
            n /= i
        if(cnt > 0):
            print(" * ",i,"^",cnt,sep='',end='')
        i+=2
    if(n > 2): print(" * ",int(n),"^1",sep='',end='')
    print()
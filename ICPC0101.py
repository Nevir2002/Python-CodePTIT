from queue import LifoQueue

n = int(input())
x = [int(x) for x in input().split()]
a = LifoQueue(maxsize=n);
for i in range(0,n):
    if (a.qsize() == 0):
        a.put(x[i]);
    else:
        tmp = a.get();
        a.put(tmp);
        if ((tmp+x[i])%2 != 0):
            a.put(x[i]);
        else:
            a.get();
print(a.qsize());
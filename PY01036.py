a = [0]*10001
a[1] = 1
a[2] = 1/2
for i in range(3,10001):
    a[i] = 1/i + a[i-2]

for t in range(int(input())):
    n = int(input())
    print(format(a[n],'.6f'))
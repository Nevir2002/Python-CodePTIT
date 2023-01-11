import math


for t in range(int(input())):
    s = [float(x) for x in input().split()]
    x = math.ceil(math.log(s[2]/s[0],1+s[1]/100))
    print(x)
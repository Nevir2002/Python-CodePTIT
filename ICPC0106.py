from xml.etree.ElementTree import tostring

def calc(s):
    res = 0
    for i in range(0,len(s)):
        res = res * 2 + int(s[i])
    if(res >= 10): return str(chr(ord('A')+res-10))
    return str(res)

t = int(input())
while t != 0:
    base = int(input())
    org = input()
    if(base == 2):
        print(org)
    else:
        n = len(org)-1
        num = []
        l = 0
        if base == 4: 
            l = 2
        elif base == 8:
            l = 3
        else:
            l = 4
        while(n >= 0):
            tmp = 0
            s = ""
            for i in range(0,l):
                if n >= 0: 
                    s = org[n] + s
                    n -= 1
                else: 
                    s = "0" + s
                    tmp = tmp * 2
            num.append(s)
        
        num.reverse()
        # for x in num:
        #     print(x,end=' ')
        # print()
        for x in num:
            print(calc(x),end='')
        print()
    
    t -= 1
# 1111100111001101
# 1111 1001 1100 1101
    
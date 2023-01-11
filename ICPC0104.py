t = int(input())
while t != 0:
    res = float('inf')
    num = 0
    str = input()
    for x in str:
        if x >= '0' and x <= '9':
            num = (num*10 + int(x))
        else:
            if num > 0 and num < res: res = num 
            num = 0
    if(num > 0 and num < res): res = num
    print(res)
    t -= 1
def product(s):

    res = 0
    for i in range(1,len(s),2):
        if int(s[i]) != 0:
            if res != 0: 
                res *= int(s[i])
            else:
                res = int(s[i])
    return res

for t in range(int(input())):
    s = input() 
    print(sum([int(x) for x in s[::2]]), product(s))
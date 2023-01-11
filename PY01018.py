P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while(True):
    try:
        k,s = input().split(maxsplit=1)
        res = ""
        for i in range(len(s)):
            x = 0
            for j in range(len(P)):
                if(P[j] == s[i]): break
                else: x += 1
            res = P[(x+int(k))%28] + res
        print(res)
    except:
        break
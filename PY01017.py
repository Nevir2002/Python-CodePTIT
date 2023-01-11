for t in range(int(input())):
    
    s = input()
    s += ' '
    cnt = 1
    for i in range(1,len(s)):
        if(s[i] == s[i-1]): cnt += 1
        else:
            print(str(cnt)+s[i-1],end='')
            cnt = 1
    print()
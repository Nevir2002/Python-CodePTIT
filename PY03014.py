for t in range(int(input())):
    s = input()
    i = 1
    res = []
    st = []
    for x in s:
        if x == '(' or x == ')':
            # print(x,i)
            if len(st) == 0 or x == '(':
                st.append(i)
                res.append(i)
                i+=1
            elif x == ')':
                tmp = st.pop()
                res.append(tmp)
    print(*res)

# 2
# (a + (b *c) ) + (d/e)
# ( ( () ) ( () ) )
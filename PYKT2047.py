from bisect import bisect_left
arr = []
while True:
    try:
        x = input().split()
        for i in x:
            arr.append(int(i))
    except:
        break
idx = 1
for t in range(arr[0]):
    n = arr[idx]
    idx += 1
    st = []
    p = [arr[i] for i in range(idx,idx+n)]
    p.append(0)
    idx += n
    h = [arr[i] for i in range(idx,idx+n)]
    idx += n
    v = [0 for i in range(n)]
    s = [0 for i in range(n)]
    s[0] = h[0]
    for i in range(1,n):
        s[i] = s[i-1] + h[i]
    # print(*s)
    v[0] = h[0]*p[0]
    st.append(0)
    for i in range(1,n):
        while len(st) > 0 and h[st[-1]] < h[i]:
            st.pop()
        v[i] = h[i]*(p[i]-(p[st[-1]] if len(st) > 0 else -1)-1)
        v[i] -= (s[i-1] - (s[st[-1]] if len(st) > 0 else 0))
        if len(st) > 0: v[i] += v[st[-1]]
        st.append(i)
    v.insert(0,0)
    # print(v)
    n = arr[idx]
    idx+=1
    for i in range(n):
        x = arr[idx]
        idx+=1
        print(bisect_left(v,x,1,len(v))-1)
    

# 1
# 4
# 1 3 5 8
# 2 5 3 1
# 7
# 17
# 3
# 13
# 1
# 2
# 15
# 16    
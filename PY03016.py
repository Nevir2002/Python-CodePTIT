from collections import defaultdict


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
cnt = defaultdict(lambda:0)
res = 0
st = []
for i in range(n):
    while len(st) > 0 and a[i] > st[-1]:
        cnt[st.pop()]-=1
        res+=1
    if len(st) > 0:
        if st[-1] == a[i]:
            res += cnt[a[i]] + (1 if len(st) > cnt[a[i]] else 0)
        else:
            res += 1
    st.append(a[i])
    cnt[a[i]]+=1
print(res)

# 7
# 2
# 4
# 1
# 2
# 2
# 5
# 1
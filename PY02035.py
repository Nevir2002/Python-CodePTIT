from collections import defaultdict


s = input()
k = int(input())
a = defaultdict(lambda:0)
for i in range(0,len(s),2):
    x = s[i:i+2]
    if(len(x) == 2): a[x]+=1
cnt = 0
for i in sorted(a.keys()):
    if a[i] >= k: 
        print(i,a[i])
        cnt+=1
if cnt == 0: print("NOT FOUND")

# 124356141111434356149
# 2
# 124356141111434356149
# 10
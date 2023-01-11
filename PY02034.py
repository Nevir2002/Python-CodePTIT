from collections import defaultdict


s = input()
a = defaultdict(lambda:0)
for i in range(0,len(s),2):
    x = s[i:i+2]
    if(len(x) == 2): a[x]+=1
for i in a.keys():
    print(i,a[i])
res = []

def generate(n,s,i,na,nb,nc):
    if i > n: return
    if na > 0 and na <= nb and nb <= nc: res.append(s)
    generate(n,s+'A',i+1,na+1,nb,nc)
    generate(n,s+'B',i+1,na,nb+1,nc)
    generate(n,s+'C',i+1,na,nb,nc+1)
def cmp(s):
    return len(s)

n = int(input())
generate(n,"",0,0,0,0)
res.sort(key=cmp)
for x in res:
    print(x)
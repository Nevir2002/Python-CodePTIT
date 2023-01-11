class mt:
    def __init__(self,id,name,method):
        self.id = id
        self.name = name
        self.method = method
class ct:
    def __init__(self,date,time,room):
        self.date = date
        self.time = time
        self.room = room
        self.dateval = date.split('/')[::-1]

class lt:
    amt = []
    act = []
    def __init__(self,str):
        a = str.split()
        self.id = a[0]
        n = int(a[0][1:])
        self.ct = lt.act[n-1]
        for i in lt.amt:
            if a[1] == i.id:
                self.mt = i
                break
        self.group = a[2]
        self.num = a[3]
    @staticmethod 
    def nextct(f):
        lt.act.append(ct(f.readline().strip(),f.readline().strip(),f.readline().strip()))
    @staticmethod     
    def nextmt(f):
        lt.amt.append(mt(f.readline().strip(),f.readline().strip(),f.readline().strip()))
    def __str__(self):
        return f'{self.ct.date} {self.ct.time} {self.ct.room} {self.mt.name} {self.group} {self.num}'

a = []
f = open("MONTHI.in","r")
t = int(f.readline().strip())
for i in range(t):
    lt.nextmt(f)
f.close()
f = open("CATHI.in","r")
t = int(f.readline().strip())
for i in range(t):
    lt.nextct(f)
f.close()
f = open("LICHTHI.in","r")
t = int(f.readline().strip())
for i in range(t):
    a.append(lt(f.readline().strip()))
f.close()
a.sort(key=lambda e:(e.ct.dateval,e.ct.time,e.id))
print(*a,sep='\n')
class ds:
    def __init__(self,date,name,num):
        # print(date,name,num)
        a = date.split()
        self.date = a[1]
        self.name = name
        self.name_splitted = name.split()
        # print(len(self.name_splitted), self.name_splitted)
        self.num = num
    def __str__(self):
        return f'{self.name}: {self.num} {self.date}'

f = open("SOTAY.txt","r")
a = []
date = f.readline().strip()
while True:
    try:
        s1 = f.readline().strip()
        # print(s1)
        if len(s1) == 0: break
        if s1.count('/') > 0:
            date = s1
        else:
            s2 = f.readline().strip()
            a.append(ds(date,s1,s2))
    except:
        break
a.sort(key=lambda e:(e.name_splitted[-1], e.name_splitted[-2]))
f.close()
f = open("DIENTHOAI.txt","w")
for i in a:
    f.writelines(i.__str__() + '\n')
f.close()

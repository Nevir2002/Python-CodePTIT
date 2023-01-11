class CT:
    def __init__(self,id,date,time,room):
        self.id = id
        self.date = date
        self.time = time
        self.room = room
        self.dateval = ''.join(self.date.split("/")[::-1])
        # print(self.dateval)
    def __str__(self):
        return f'{self.id} {self.date} {self.time} {self.room}'
f = open("CATHI.in",'r')
a = [CT(f'C{i+1:03d}',f.readline().strip(),f.readline().strip(),f.readline().strip()) for i in range(int(f.readline()))]
a.sort(key=lambda e: (e.dateval,e.time))
print(*a,sep='\n')

# 2
# 09/01/2022
# 15:30
# 70172
# 09/01/2022
# 10:00
# 70279
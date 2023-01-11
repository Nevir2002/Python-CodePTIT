class KH:
    def __init__(self,id,name,input):
        s = input.split()
        self.id = id
        self.name = ' '.join(name.strip().title().split())
        cap = 0
        if s[0] == 'A': cap = 100
        if s[0] == 'B': cap = 500
        if s[0] == 'C': cap = 200
        diff = int(s[2]) - int(s[1])
        self.org = 0
        self.add = 0
        self.vat = 0
        self.total = 0
        if diff > cap:
            self.add = (diff-cap)*1000
            diff = cap
        self.org = diff*450
        self.vat = self.add//20
        self.total = self.org + self.add + self.vat
    def __str__(self):
        return f'{self.id} {self.name} {self.org} {self.add} {self.vat} {self.total}'

print(*sorted([KH(f'KH{i+1:02d}',input(),input()) for i in range(int(input()))],key=lambda e:-e.total),sep='\n')

# 2
#  nGuyEn Hong Ngat
# C 200 278
#  Chu thi    minh
# A 120 160
class NV:
    PB_id = []
    PB_name = []
    def __init__(self,id,name,daily,num):
        self.id = id
        self.name = name
        coeff = 0
        if id[:1] == 'A':
            years = int(id[1:3])
            if years <= 3: coeff = 10
            elif years <= 8: coeff = 12
            elif years <= 15: coeff = 14
            else: coeff = 20
        if id[:1] == 'B':
            years = int(id[1:3])
            if years <= 3: coeff = 10
            elif years <= 8: coeff = 11
            elif years <= 15: coeff = 13
            else: coeff = 16
        if id[:1] == 'C':
            years = int(id[1:3])
            if years <= 3: coeff = 9
            elif years <= 8: coeff = 10
            elif years <= 15: coeff = 12
            else: coeff = 14
        if id[:1] == 'D':
            years = int(id[1:3])
            if years <= 3: coeff = 8
            elif years <= 8: coeff = 9
            elif years <= 15: coeff = 11
            else: coeff = 13
        for i in range(len(NV.PB_id)):
            if NV.PB_id[i] == id[-2:]:
                self.pb = NV.PB_name[i]
                break
        self.total = int(num) * coeff * int(daily)*1000
    def __str__(self):
        return f'{self.id} {self.name} {self.pb} {self.total}'
    def add_pb(s):
        a = s.split()
        NV.PB_id.append(a[0])
        NV.PB_name.append(' '.join(a[1:]))
for t in range(int(input())):
   NV.add_pb(input()) 
for t in range(int(input())):
    print(NV(input(),input(),input(),input()))

# 2
# HC Hanh chinh
# KH Ke hoach Dau tu
# 2
# C06HC
# Tran Binh Minh
# 65
# 25
# D03KH
# Le Hoa Binh
# 59
# 24
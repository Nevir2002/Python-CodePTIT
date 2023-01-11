class LT:
    MT_id = []
    MT_name = []
    def __init__(self,id,input):
        s = input.strip().split()
        self.id = id
        self.mt_id = s[0]
        self.mt_name = 'null'
        for i in range(len(LT.MT_id)):
            if LT.MT_id[i] == s[0]:
                self.mt_name = LT.MT_name[i]
                break
        self.date = s[1]
        self.time = s[2]
        self.dateval = ''.join(s[1].split("/")[::-1])
        self.group = s[3]
    def __str__(self):
        return f'{self.id} {self.mt_id} {self.mt_name} {self.date} {self.time} {self.group}'
n,t = [int(x) for x in input().split()]
for i in range(n):
    LT.MT_id.append(input().strip())
    LT.MT_name.append(input().strip())
a = sorted([LT(f'T{i+1:03d}',input()) for i in range(t)],key=lambda e:(e.dateval,e.time,e.mt_id))
print(*a,sep='\n')


# 2 10
# INT1155
# Tin hoc co so 2
# INT1339
# Ngon ngu lap trinh C++
# INT1155 25/11/2021 08:00 01
# INT1155 04/12/2021 08:00 02
# INT1155 04/12/2021 13:30 03
# INT1155 25/11/2021 13:30 04
# INT1155 25/11/2021 15:00 05
# INT1339 25/11/2021 08:00 01
# INT1339 25/11/2021 08:00 02
# INT1339 04/12/2021 13:30 03
# INT1339 04/12/2021 13:30 04
# INT1339 04/12/2021 15:00 05
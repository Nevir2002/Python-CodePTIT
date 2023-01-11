class SV:
    def __init__(self,id,name,p1,p2,p3):
        self.id = id
        self.name = ' '.join(name.strip().title().split())
        # self.avg = round(((Decimal(p1)*3+Decimal(p2)*3+Decimal(p3)*2)/(3+3+2)*100)+Decimal(0.001))/100
        self.avg = (float(p1)*3+float(p2)*3+float(p3)*2)/(3+3+2)+0.001
        self.rank = 0
    def __str__(self):
        return f'{self.id} {self.name} {self.avg:.2f} {self.rank}'
    def set_rank(self,i):
        self.rank = i
a = [SV(f'SV{i+1:02d}',input(),input(),input(),input()) for i in range(int(input()))]
a.sort(key=lambda e:(-e.avg,e.id))
a[0].set_rank(1)
for i in range(1,len(a)):
    a[i].set_rank(a[i-1].rank if a[i].avg == a[i-1].avg else i+1)
print(*a,sep='\n')


# 2
#  ha Thi kieu     anh
# 7
# 6
# 7
# Pham    THI  HAO
# 6
# 7
# 6
# nbt
# 6
# 7
# 6
# xyz
# 7
# 6
# 6
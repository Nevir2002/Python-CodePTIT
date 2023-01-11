class TS:
    def __init__(self,id,name,pts,race,region):
        self.id = id
        self.name = ' '.join(name.strip().title().split())
        bonus = 0
        if region == '1': bonus += 1.5
        elif region == '2': bonus += 1
        if race != 'Kinh': bonus += 1.5
        self.pts = float(pts) + bonus
        self.status = "Do" if self.pts >= 20.5 else "Truot"
    def __str__(self):
        return f'{self.id} {self.name} {self.pts:.1f} {self.status}'
print(*sorted([TS(f'TS{i+1:02d}',input(),input(),input(),input()) for i in range(int(input()))],key=lambda e:(-e.pts,e.id)),sep='\n')


# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3
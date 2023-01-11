class Movie:
    category_name = []
    def __init__(self,id,category,date,name,episodes):
        self.id = id.strip()
        self.category = Movie.category_name[int(category[2:])-1]
        self.date = date.strip()
        self.name = name.strip()
        self.episodes = int(episodes.strip())
        self.dateval = ''.join(self.date.split("/")[::-1])
    def __str__(self):
        return f'{self.id} {self.category} {self.date} {self.name} {self.episodes}'
m,n = [int(x) for x in input().split()]
for i in range(m):
    Movie.category_name.append(input().strip())
a = [Movie(f'P{i+1:03d}',input(),input(),input(),input()) for i in range(n)]
a.sort(key=lambda e:(e.dateval,e.name,-e.episodes))
print(*a,sep='\n')

# 2 3
# Hai huoc
# Tinh cam
# TL001
# 25/11/2021
# Phim so 1
# 10
# TL001
# 04/12/2021
# Phim so 2
# 15
# TL002
# 25/11/2021
# Phim so 3
# 5
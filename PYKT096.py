class Team:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __str__(self):
        return f'{self.id} {self.name}'
class TS:
    team_list = []
    def __init__(self,id,name,team_id):
        self.id = id
        self.name = name
        team_idx = int(team_id[-2:])-1
        self.team = TS.team_list[team_idx]
    def __str__(self):
        return f'{self.id} {self.name} {self.team}'
for t in range(int(input())):
    TS.team_list.append(Team(input(),input()))
# print(len(TS.team_list))
print(*sorted([TS(f'C{i+1:03d}',input(),input()) for i in range(int(input()))],key=lambda e:e.name),sep='\n')

# 2
# BAV_MIS
# Banking Academy of Vietnam
# FTU Knights1
# Foreign Trade University
# 6
# Le Trung Toan
# Team01
# Nguyen Trinh Quoc Long
# Team01
# Giang Minh Tung
# Team01
# Nguyen Hang Giang
# Team02
# Nguyen Thanh Nhan
# Team02
# Nguyen Viet Duc
# Team02
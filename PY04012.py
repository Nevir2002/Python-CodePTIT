class stud:
    def __init__(self,id,name,cls):
        self.id = id
        self.name = name
        self.cls = cls
        self.mark = 10
        self.status = ''
    def input(self,s):
        for x in s:
            if x == 'v': self.mark -= 2
            if x == 'm': self.mark -= 1
        self.mark = max(self.mark,0)
        if self.mark == 0: self.status = "KDDK"
    def __str__(self):
        return f'{self.id} {self.name} {self.cls} {self.mark} {self.status}'

t = int(input())
a = [stud(input(),input(),input()) for i in range(t)]
for i in range(t):
    id,s = input().split()
    for i in a:
        if i.id == id:
            i.input(s)
            break
print(*a,sep='\n')


# 3
# B19DCCN999
# Le Cong Minh
# D19CQAT02-B
# B19DCCN998
# Tran Truong Giang
# D19CQAT02-B
# B19DCCN997
# Nguyen Tuan Anh
# D19CQCN04-B
# B19DCCN998 xxxmxmmvmx
# B19DCCN997 xmxmxxxvxx
# B19DCCN999 xvxmxmmvvm
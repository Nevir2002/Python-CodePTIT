from random import choice
choices = [0,1,2]
eggs = [43,33,23]
for i in range(3):
    eggs = [43,33,23]
    eggs[i]+=1
    while sum(eggs) > 1:
        minIndex = eggs.index(min(eggs))
        for j in range(3):
            if j == minIndex: eggs[j]+=1
            else: eggs[j]-=1
    print(eggs)
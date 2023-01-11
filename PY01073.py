from itertools import permutations

s = input()
for i in list(permutations(s)):
    print("".join(i))
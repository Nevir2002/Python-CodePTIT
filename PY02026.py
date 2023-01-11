irrelevant = input()
a = sorted(list(set([int(x) for x in input().split()])))
b = sorted(list(set([int(x) for x in input().split()])))
# print(a)
# print(b)
print("YES" if a == b else "NO")

# 12 18
# 1 2 3 4 5 1 2 3 5 4 1 2
# 1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5
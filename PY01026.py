from collections import defaultdict


def check(s1,s2):
	a = defaultdict(lambda:0)
	b = defaultdict(lambda:0)
	for i in s1: a[i]+=1
	for i in s2: b[i]+=1
	return a == b

for t in range(int(input())):
	print(f'Test {t+1}: {"YES" if check(input(),input()) else "NO"}')

# 4
# testing
# intestg
# abc
# aabbbcccc
# abcabcbcc
# aabbbcccc
# abc
# xyz
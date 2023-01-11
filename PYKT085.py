from collections import defaultdict


a = defaultdict(lambda:0)
flag = True
currS = ''
for t in range(int(input())):
	s = input().strip()
	if len(s) == 0: flag = True
	elif flag:
		flag = False
		currS = s
	elif not flag:
		a[currS] += 1

for i in a.keys(): print(f'{i}: {a[i]}')

# 9
# Home/accommodation
# What kind of housing/accommodation do you live in?
# Who do you live with?
# How long have you lived there?

# Study
# Describe your education
# What is your area of specialization?
# Why did you choose to study that major?
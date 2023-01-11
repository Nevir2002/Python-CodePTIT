import re
res = ''
while(True):
	try:
		s = input().lower().split()
		for i in s:
			if i[-1] == '.' or i[-1] == '?' or i[-1] == '!':
				i = i[0:-1:1]
				res += i
				print(res[0].upper(),end='')
				print(res[1::])
				res = ''
			else: res += i + ' '
		# if(s[0] == '0'): break

	except:
		break
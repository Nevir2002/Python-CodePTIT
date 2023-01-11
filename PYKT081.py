def check(s):
	if len(s) != 4: return False
	for i in s:
		if not i.isdigit(): return False
		if int(i) < 0 or int(i) > 255: return False
	return True

for t in range(int(input())):
	s = input().split('.')
	print("YES" if check(s) else "NO")

# 3
# 192.168.1.1
# 256.255.255.255
# 113.123.121.x31
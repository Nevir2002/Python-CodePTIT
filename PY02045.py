s = input()
while True:
    n = len(s)
    a = s[:n//2]
    b = s[n//2:]
    s = str((int(a)+int(b)))
    print(s)
    if len(s) == 1: break
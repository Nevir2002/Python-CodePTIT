def check(a):
    b = a[::-1]
    for i in range(len(a)):
        if abs(ord(a[i]) - ord(a[i-1])) != abs(ord(b[i]) - ord(b[i-1])): return False
    return True

for t in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")
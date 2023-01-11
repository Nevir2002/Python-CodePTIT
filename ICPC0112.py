t = int(input())

def sieve(prime,n):
    p = 2
    while p*p <= n:
        if prime[p] == True:
            i = p*2
            while i <= n:
                prime[i] = False
                i += p
        p += 1

while t != 0:
    n = int(input())
    prime = [True] * (n+1)
    sieve(prime,n)
    res = 0
    for i in range(2, n-5):
        if prime[i] and prime[i+2] and prime[i+6] or prime[i] and prime[i+4] and prime[i+6]:
            res += 1
    print(res)

    t -= 1
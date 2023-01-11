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
    
    for i in range(n):
        if(prime[i]):
            iv = str(i)[::-1]
            if int(iv) <= n and prime[int(iv)] and str(i) != iv:
                print(i,iv,end=" ")
                prime[i] = prime[int(iv)] = False
    print()

    t -= 1
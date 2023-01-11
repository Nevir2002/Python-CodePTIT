def rec(n,a,c,b):
    if(n == 0): 
        return
    rec(n-1,a,b,c)
    print(a + " -> " + c)
    rec(n-1,b,c,a)

rec(int(input()),'A','C','B')
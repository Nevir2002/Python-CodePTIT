for t in range(int(input())):
    n = input()
    product = 1
    for i in range(len(n)):
        if n[i] != '0':product *= int(n[i])
    print(product)
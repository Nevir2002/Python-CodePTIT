for t in range(int(input())):
    
    d,m = [int(x) for x in input().split()]
    n = m*31+d
    if n >= 1*31+20 and n <= 2*31+18: print("Bao Binh")
    elif n >= 2*31+19 and n <= 3*31+20: print("Song Ngu")
    elif n >= 3*31+21 and n <= 4*31+19: print("Bach Duong")
    elif n >= 4*31+20 and n <= 5*31+20: print("Kim Nguu")
    elif n >= 5*31+21 and n <= 6*31+20: print("Song Tu")
    elif n >= 6*31+21 and n <= 7*31+22: print("Cu Giai")
    elif n >= 7*31+23 and n <= 8*31+22: print("Su Tu")
    elif n >= 8*31+23 and n <= 9*31+22: print("Xu Nu")
    elif n >= 9*31+23 and n <= 10*31+22: print("Thien Binh")
    elif n >= 10*31+23 and n <= 11*31+22: print("Thien Yet")
    elif n >= 11*31+23 and n <= 12*31+21: print("Nhan Ma")
    else: print("Ma Ket")
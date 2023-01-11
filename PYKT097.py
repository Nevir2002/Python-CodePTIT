while True:
    try:
        s = input()
        # if(s == '0'): break
        a = s.strip().lower().split()
        a[0] = a[0].title()
        for i in range(len(a)-1):
            if a[i+1] == '.' or a[i+1] == '!' or a[i+1] == '?':
                a[i] += a[i+1]
                a.pop(i+1)
        print(*a, end='')
        print('.' if not (a[-1][-1] == '.' or a[-1][-1] == '!' or a[-1][-1] == '?') else '')
    except:
        break

# Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.
# co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
# muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
# moi    CAC BAN danG ky     thaM giA !
nam=int(input("nhap nam bat ky:"))
if nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0:
    print("la nam nhuan")
else:
    print("khong phai la nam nhuan")
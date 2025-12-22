w=float(input("nhap chieu rong(gioi han 100):"))
h=float(input("nhap chieu dai(gioi han 100):"))
while True:
    w=float(input("nhap chieu rong (gioi han 100):"))
    if w > 0 and w <= 100:
        break
    else:
        print("sai,Nhap lai")
while True:
    h=float(input("nhap chieu dai (gioi han 100):"))
    if h > 0 and h <= 100:
        break
    else:
        print("sai,Nhap lai")
chu_vi=(w+h)*2
dien_tich=w*h
print(f"Chu vi hcn la:",chu_vi)
print(f"Dien tich hcn la:",dien_tich)
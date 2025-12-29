x=float(input("nhap diem mon toan:"))
y=float(input("nhap diem mon ly:"))
z=float(input("nhap diem mon hoa:"))
tong=x+y+z
if tong >= 15 and x > 4 and y > 4 and z > 4:
    print("hoc deu cac mon")
elif x > 4 and y > 4 and z < 4:
    print("hoc chua deu cac mon")
else:
    print("thi hong")
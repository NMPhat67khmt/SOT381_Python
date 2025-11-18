a=input("nhap so dau tien:")
b=input("nhap so thu hai:")
phep=input("chon phep tinh sau(=,-,*,/)")
if phep == "+":
   print("Ket qua:", a + b)
elif phep == "-":
    print("ket qua:", a - b)
elif phep == "*":
    print("Ket qua:", a * b)
elif phep == "/":
    if b != 0:
           print("Ket qua:", a / b)
    else:
        print("Khong the chia cho 0")
else:
    print("Phep toan nay bo tay")
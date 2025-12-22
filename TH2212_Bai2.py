so_lon_nhat=int(input("nhap so lon nhat"))
so_nho_nhat=int(input("nhap so nho nhat"))
a=int(input("nhap so a:"))
b=int(input("nhap so b:"))
c=int(input("nhap so c:"))
if a > so_lon_nhat:
    so_lon_nhat=a
elif b > so_lon_nhat:
       so_lon_nhat=b
elif c > so_lon_nhat:
        so_lon_nhat=c
if a < so_nho_nhat:
    so_nho_nhat=a
elif b < so_nho_nhat:
        so_nho_nhat=b
elif c < so_nho_nhat:
        so_nho_nhat=c
print(f"So lon nhat la:",so_lon_nhat)
print(f"So nho nhat la:",so_nho_nhat)
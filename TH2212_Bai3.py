def so_lon_nhat(a,b,c):
    so_lon_nhat = a
    if b > so_lon_nhat:
        so_lon_nhat=b
    if c>so_lon_nhat:
       so_lon_nhat=c
    return so_lon_nhat

a=int(input("nhap so a:"))
b=int(input("nhap so b:"))
c=int(input("nhap so c:"))
print("so lon nhat la:", so_lon_nhat(a,b,c))
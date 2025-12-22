def so_lon_nhat_va_so_nho_nhat(a,b,c):
    so_lon_nhat = a
    if b > so_lon_nhat:
        so_lon_nhat=b
    if c>so_lon_nhat:
        so_lon_nhat=c
    so_nho_nhat = a
    if b < so_nho_nhat:
        so_nho_nhat=b
    if c < so_nho_nhat:
        so_nho_nhat=c
    return so_lon_nhat,so_nho_nhat

a=int(input("nhap so a:"))
b=int(input("nhap so b:"))
c=int(input("nhap so c:"))
numMax, numMin= so_lon_nhat_va_so_nho_nhat(a,b,c)
print(f"so lon nhat la {numMax}")
print(f"so nho nhat la {numMin}")

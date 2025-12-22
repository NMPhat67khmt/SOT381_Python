def tong(n):
    x=0
    for i  in range(1,n+1):
        x+=i
    y=0
    for i in range(2,n+1,2):
        y+=i
    S=x/y
    return S
n=int(input("nhap so n:"))
gia_tri_cua_S= tong(n)
print(gia_tri_cua_S)
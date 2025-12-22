n=int(input("nhap so luong phan tu"))
ds=[]
for i in range(n):
    x=int(input((f"nhap phan tu",i+1)))
    ds.append(x)
so_lon_nhat=max(ds)
so_nho_nhat=min(ds)
print("Danh sach:", ds)
print("So lon nhat:", so_lon_nhat)
print("So nho nhat:", so_nho_nhat)
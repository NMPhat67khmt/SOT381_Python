n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    x = int(input(f"Nhap phan tu:"))
    ds.append(x)
ds_tang = sorted(ds)
print("Danh sach ban dau:", ds)
print("Danh sach tang dan:", ds_tang)

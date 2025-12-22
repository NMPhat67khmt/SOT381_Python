# Xóa tất cả phần tử có giá trị x trong List
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    x = int(input(f"Nhap phan tu:"))
    ds.append(x)
ds_rong=ds.clear()
print("danh sach ban dau",ds)
print("danh sach rong",ds_rong)
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    x = int(input(f"Nhap phan tu:"))
    ds.append(x)
ds_dao = ds[::-1]

print(ds)
print("dao nguoc cua ds:", ds_dao)
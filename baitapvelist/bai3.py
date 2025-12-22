n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    x = int(input(f"Nhap phan tu:"))
    ds.append(x)
so_chan = 0
so_le = 0
for x in ds:
    if x % 2 == 0:
        so_chan += 1
    else:
        so_le += 1
print("Danh sach:", ds)
print("So luong so chan:", so_chan)
print("So luong so le:", so_le)
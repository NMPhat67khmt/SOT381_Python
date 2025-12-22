# Gộp hai List số nguyên thành một List mới
n = int(input("Nhap so luong phan tu cho danh sach dau tien: "))
ds1 = []
for i in range(n):
    x = int(input(f"Nhap phan tu:"))
    ds1.append(x)
m = int(input("Nhap so luong phan tu cho danh sach thu hai: "))
ds2 = []
for i in range(m):
    y = int(input(f"Nhap phan tu:"))
    ds2.append(y)
combined= ds1 + ds2
print("Danh sach 1:", ds1)
print("Danh sach 2:", ds2)
print("Danh sach sau khi gop:", combined)
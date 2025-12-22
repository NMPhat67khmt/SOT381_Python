n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    x = int(input(f"Nhap phan tu:"))
    ds.append(x)
m= int(input("Nhap so can kiem tra:"))
if m in ds:
    print(f"Co trong danh sach")
    print("Vi tri xuat hien:")
    for i in range(len(ds)):
        if ds [i] == m:
            print(i)
else:
    print("khong co trong danh sach")
            
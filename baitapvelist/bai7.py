#Tính điểm trung bình của List điểm số
n = int(input("Nhap so luong diem: "))
ds = []
for i in range(n):
    x = float(input(f"Nhap phan tu:"))
    ds.append(x)
diem_trung_binh= sum(ds)/len(ds)
print("Danh sach diem:", ds)
print("Điểm trung binh:", diem_trung_binh)
    
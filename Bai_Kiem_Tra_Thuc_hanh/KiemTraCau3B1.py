n=int(input("nhap so luong phan tu n:"))
ds=[]
for x in range(n):
    x=int(input("nhap phan tu:"))
    ds.append(x)

print("cac phan tu chua het cho 2 va 3 la:")
for x in ds:
    if x % 2 == 0 and x % 3 == 0:
        print(x,f"")

n=int(input("nhap so luong phan tu"))
ds=[]
for i in range(n):
    x=int(input(("nhap phan tu thu",i+1)))
ds.append(x)
          
tong=sum(ds)
print("Danh sách:", ds)
print("Tổng =", tong)
          
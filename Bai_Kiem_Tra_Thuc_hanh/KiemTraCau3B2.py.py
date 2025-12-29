n=int(input("nhap so luong phan tu n:"))
ds=[]
for x in range(n):
    x=int(input("nhap phan tu:"))
    ds.append(x)
    
tong=0
for x in ds:
    if x % 2 == 0 or x % 3 == 0:
       tong+=x
        
print("Tong cac phan tu chia het cho 2 hoac 3 la:", tong)
dsbh=[]
n=int(input("nhap so luong bai hat"))
for i in range(n):
    tenbaihat=input(f"nhap ten bai hat {i+1}")
    dsbh+=[tenbaihat]
for i in range(len(dsbh)):
    print("Bai" ,i,'la',dsbh[i])
for bai in dsbh:  
    print(bai)
    
for i in range(n):
    ten=dsbh[i]
    TEN=ten.upper
    print(TEN)
    
print("cac bai co tu yeu:")
for i in range(n):
    ten=dsbh[i]
    if ten.find("yeu"):
        print(ten)
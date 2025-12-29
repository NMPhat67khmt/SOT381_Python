def is_armstrong(n):
    if n < 0:
        return False
    str_n = str(n)
    k = len(str_n)
    total = 0
    for digit in str_n:
        total += int(digit) ** k
    return total == n
      
n=int(input("nhap so luong phan tu n:"))
ds=[]
for i in range(n):
    x=int(input("nhap phan tu:"))
    ds.append(x)

count = 0
print(f"Cac so Armstrong trong danh sach:")
for x in ds:
    if is_armstrong(x):
        print(x)
        count += 1
print("So luong so Armstrong:", count)
import math
a=int(input("nhap canh a:"))
b=int(input("nhap canh b:"))
c=int(input("nhap canh a:"))
if a + b > c and b + c > a and a + c > b:
    print("ba canh nay da tao dc tam giac")
if a == b and b == c:
    print("Tam giac deu")
elif a == b and a == c and b == c:
    print("tam giac can")
elif (math.isclose(a**2 + b**2, c**2) or math.isclose(a**2 + c**2, b**2) or math.isclose(b**2 + c**2, a**2)):
    print("tam giac vuong")
else:
    print("tam giac thuong")
    
    
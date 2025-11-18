cannang=int(input("How heavy are you?:"))
chieucao=int(input("How tall are you?(tinh theo M):"))
BMI= (cannang / chieucao) * chieucao
if BMI < 18.5:
    print("ban gay qua an nhieu len")
elif BMI < 24.9:
    print("ok roi day, binh thuong do")
elif BMI > 25:
    print("an it thoi, beo lam roi")

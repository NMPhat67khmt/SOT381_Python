dautu=100000000
laisuat=0.07
for i in range(1,6):
    S = dautu * (1+laisuat) ** i
    print(f"Số tiền sau {i} năm: {S:.2f} VND")

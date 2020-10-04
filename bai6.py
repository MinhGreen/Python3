import math
n = int(input("Nhập bán kính : "))
def DienTichHinhTron(r):
    s=math.pi*r*r
    return s
print(f"Diện tích hình tròn có bán kính {n}: {DienTichHinhTron(n)}")
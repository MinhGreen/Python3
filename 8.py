# Tinh tong so nguyen to
import math
def snt(n):
    if n<2:
        return 0
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n=int(input("Nhap n:"))
def tongsnt(n):
    s=0
    for i in range(1,n+1):
        if snt(i):
            s+=i
    print(f"Tong cac so nguyen to: {s}")
tongsnt(n)
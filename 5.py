#TỔNG CÁC SỐ CHẴN
def Tongchan():
  n= int(input("Nhập số chẵn: "))
  x = 0
  while n % 2 !=0:
    n= int(input("Nhập lại: "))
  for i in range(n):
     i += 1
     if i % 2 == 0:
      x += i
  print(x)
Tongchan()
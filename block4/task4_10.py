from math import pi

x = int(input("Введите число x:"))

y = int(input("Введите число y:"))
S1 = x*x 
print("Площадь квадрата")
S2 = y*y*pi
print("Площадь круга")
if S1>S2: 
    print(f" Площадь квадрата больше площади круга")
else:
   print("Площадь квадрата меньше площади круга")


print(S1,S2)
from math import sin

x = float(input("Введите значение x: "))

if x > 0:
    y = sin(x**2)
else:
    y = 1 + 2 * (sin(x)**2)
    print(y)

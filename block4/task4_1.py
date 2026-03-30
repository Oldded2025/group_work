from math import sin


x = int(input("Введите х: "))

if x > 0:
    y = sin(x) * sin(x)
else:
    y = 1 - 2 * sin(x * x)

print(y)

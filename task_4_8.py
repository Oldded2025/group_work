km = float(input("Введите расстояние в километрах: "))
feet = float(input("Введите расстояние в футах: "))

meters_from_km = km * 1000
meters_from_feet = feet * 0.305


if meters_from_km < meters_from_feet:
    print("расстояние в километрах меньше")
elif meters_from_feet < meters_from_km:
    print("расстояние в футах меньше")
else:
    print("Расстояния равны")


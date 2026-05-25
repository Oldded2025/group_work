# Ввод номера года
year_number = int(input("Введите номер года: "))

# Проверка условия високосности согласно правилу:
# 1. Год високосный, если он кратен 4
# 2. Но если он кратен 100, то он високосный ТОЛЬКО когда кратен 400

is_leap_year = False  # предполагаем, что год не високосный

# Проверяем условие
if year_number % 4 != 0:
    # Не кратен 4 -> не високосный
    is_leap_year = False
elif year_number % 100 != 0:
    # Кратен 4, но не кратен 100 -> високосный
    is_leap_year = True
elif year_number % 400 == 0:
    # Кратен 400 -> високосный
    is_leap_year = True
else:
    # Кратен 100, но не кратен 400 -> не високосный
    is_leap_year = False

# Вывод результата
print("\n" + "=" * 40)
print(f"Год: {year_number}")

if is_leap_year:
    print(f"РЕЗУЛЬТАТ: Год {year_number} является ВИСОКОСНЫМ.")
    print(f"  - Он содержит 366 дней.")
    print(f"  - Февраль имеет 29 дней.")
else:
    print(f"РЕЗУЛЬТАТ: Год {year_number} является НЕВИСОКОСНЫМ.")
    print(f"  - Он содержит 365 дней.")
    print(f"  - Февраль имеет 28 дней.")

print("=" * 40)

# Дополнительная информация о проверке
print("\nПроверка по правилам:")
if year_number % 4 != 0:
    print(f"  • {year_number} не кратен 4 → не високосный")
else:
    print(f"  • {year_number} кратен 4 → возможен вариант")
    if year_number % 100 != 0:
        print(f"  • {year_number} не кратен 100 → високосный")
    else:
        print(f"  • {year_number} кратен 100 → требуется дополнительная проверка")
        if year_number % 400 == 0:
            print(f"  • {year_number} кратен 400 → високосный")
        else:
            print(f"  • {year_number} не кратен 400 → не високосный")
            
class Rectangle:
    """Класс для представления прямоугольника со сторонами, параллельными осям координат."""
    
    def __init__(self, x, y, width, height):
        """
        Инициализация прямоугольника.
        
        Параметры:
        x, y - координаты левого нижнего угла
        width - ширина (по оси X)
        height - высота (по оси Y)
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # Вычисляем координаты правого верхнего угла для удобства
        self.x_right = x + width
        self.y_top = y + height
    
    def contains_point(self, px, py):
        """Проверяет, принадлежит ли точка (px, py) прямоугольнику."""
        return (self.x <= px <= self.x_right) and (self.y <= py <= self.y_top)
    
    def contains_rectangle(self, other):
        """
        Проверяет, принадлежат ли все точки другого прямоугольника текущему.
        То есть, содержится ли other полностью внутри self.
        """
        return (self.x <= other.x and self.x_right >= other.x_right and
                self.y <= other.y and self.y_top >= other.y_top)
    
    def intersects(self, other):
        """
        Проверяет, пересекаются ли прямоугольники (имеют хотя бы одну общую точку).
        """
        # Прямоугольники не пересекаются, если один находится слева, справа, снизу или сверху от другого
        if (self.x_right < other.x or other.x_right < self.x or
            self.y_top < other.y or other.y_top < self.y):
            return False
        return True
    
    def __str__(self):
        """Строковое представление прямоугольника."""
        return f"Прямоугольник: левый нижний ({self.x}, {self.y}), правый верхний ({self.x_right}, {self.y_top})"


def get_rectangle_input(rect_name):
    """Ввод данных прямоугольника с проверкой."""
    print(f"\nВведите данные для {rect_name} прямоугольника:")
    x = float(input(f"  x (координата левого нижнего угла): "))
    y = float(input(f"  y (координата левого нижнего угла): "))
    width = float(input(f"  ширина (по оси X, >0): "))
    height = float(input(f"  высота (по оси Y, >0): "))
    
    if width <= 0 or height <= 0:
        print("  Ошибка: ширина и высота должны быть положительными. Установлены значения по умолчанию 1.")
        width = abs(width) if width != 0 else 1
        height = abs(height) if height != 0 else 1
    
    return Rectangle(x, y, width, height)


# Основная программа
print("=" * 60)
print("ЗАДАЧА: Два прямоугольника, стороны параллельны осям координат")
print("=" * 60)

# Ввод данных
rect1 = get_rectangle_input("ПЕРВОГО")
rect2 = get_rectangle_input("ВТОРОГО")

# Вывод информации о прямоугольниках
print("\n" + "-" * 60)
print("Исходные данные:")
print(f"  {rect1}")
print(f"  {rect2}")
print("-" * 60)

# а) Принадлежат ли все точки первого прямоугольника второму?
print("\nа) Все точки ПЕРВОГО прямоугольника принадлежат ВТОРОМУ?")
if rect2.contains_rectangle(rect1):
    print(f"   ДА. Второй прямоугольник полностью содержит первый.")
else:
    print(f"   НЕТ. Не все точки первого прямоугольника принадлежат второму.")

# б) Принадлежат ли все точки одного из прямоугольников другому?
print("\nб) Все точки одного из прямоугольников принадлежат другому?")
if rect1.contains_rectangle(rect2):
    print(f"   ДА. Первый прямоугольник полностью содержит второй.")
elif rect2.contains_rectangle(rect1):
    print(f"   ДА. Второй прямоугольник полностью содержит первый.")
else:
    print(f"   НЕТ. Ни один из прямоугольников полностью не содержит другой.")
    print(f"   (Они либо пересекаются частично, либо не пересекаются вообще.)")

# в) Пересекаются ли эти прямоугольники?
print("\nв) Пересекаются ли прямоугольники?")
if rect1.intersects(rect2):
    print(f"   ДА. Прямоугольники пересекаются (имеют хотя бы одну общую точку).")
    
    # Дополнительная информация о характере пересечения
    if rect1.contains_rectangle(rect2) or rect2.contains_rectangle(rect1):
        print(f"   При этом один прямоугольник полностью находится внутри другого.")
    else:
        print(f"   Прямоугольники пересекаются частично.")
else:
    print(f"   НЕТ. Прямоугольники не пересекаются.")

print("\n" + "=" * 60)

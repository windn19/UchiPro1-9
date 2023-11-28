#  Напиши программу, в которой создай классы: Rectangle (прямоугольник), Circle (окружность),
#  Triangle (произвольный треугольник), RightTriangle (прямоугольный треугольник). Прямоугольник задается
#  двумя сторонами, окружность — радиусом, треугольник — тремя сторонами, прямоугольный треугольник — двумя катетами.
#  Реализуй в классах следующие методы:
#     • get_area() — возвращает целое число (если результат получается не целый,
#     то округлить к ближайшему целому) — площадь;
#     • get_perimeter() — возвращает целое число (если результат получается не целый,
#     то округлить к ближайшему целому) — периметр;
#     • __str__() — возвращает название класса.
#
# При создании классов избегай лишнего дублирования кода, используй наследование и полиморфизм.
# Считай с клавиатуры 2 строки. На первой строке указано название класса: Rectangle, Circle, Triangle
# или RightTriangle. На второй строке записано одно или несколько целых чисел через пробел — необходимые параметры
# для данного экземпляра класса. Выведи строковое представление объекта, а также площадь и периметр на разных строках.
#
# Входные данные:
# Две строки - название класса и одно или несколько целых чисел через пробел.
# Выходные данные:
# Выводится 3 строки.
#
# Пример работы программы:
# tr = RightTriangle(3, 4)
# print(tr)
# print(tr.get_area())
# print(tr.get_perimeter())
# Вывод
# RightTriangle
# 6
# 12
#
# Пример ввода:
# Triangle
# 4 5 6
# Пример вывода:
# Triangle
# 10
# 15

class Shape:
    def __str__(self):
        return self.__class__.__name__


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimter(self):
        return 2 * (self.a + self.b)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return round(3.14 * self.r ** 2)

    def get_perimter(self):
        return round(2 * 3.14 * self.r)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5)

    def get_perimter(self):
        return self.a + self.b + self.c


class RightTriangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return round(self.a * self.b / 2)

    def get_perimter(self):
        c = (self.a ** 2 + self.b ** 2) ** 0.5
        return round(self.a + self.b + c)


s = input()
if s == 'Rectangle':
    a, b = map(int, input().split())
    shape = Rectangle(a, b)
elif s == 'Circle':
    r = int(input())
    shape = Circle(r)
elif s == 'Triangle':
    a, b, c = map(int, input().split())
    shape = Triangle(a, b, c)
else:
    a, b = map(int, input().split())
    shape = RightTriangle(a, b)
print(shape)
print(shape.get_area())
print(shape.get_perimter())

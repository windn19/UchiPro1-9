class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Прямоугольник со сторонами {self.a} {self.b}'

    def get_area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def __str__(self):
        return f'Квадрат со стороной {self.a}'


s = Square(5)
p = Rectangle(4, 5)
print(p)
print(s)
print(s.get_area())
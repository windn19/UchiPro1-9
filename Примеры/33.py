class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r ** 2


# shape_1 = Rectangle(5, 6)
# shape_2 = Circle(4)
# print(shape_1.get_area())  # 30
# print(shape_2.get_area())  # 50.24
shapes = [Rectangle(6, 6), Circle(8)]
for item in shapes:
    print(f'Площадь: {item.get_area()}')
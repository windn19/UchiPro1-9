class Rectangle:
    pass


class Square(Rectangle):
    pass


print(issubclass(Rectangle, object))  # True
print(issubclass(Square, object))  # True
print(issubclass(Square, Rectangle))  # True
print(issubclass(Rectangle, Square))  # False

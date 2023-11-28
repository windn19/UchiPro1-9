# Напиши программу, в которой создай классы:
#     • Bin (число в двоичной системе счисления);
#     • Oct (число в восьмеричной системе счисления);
#     • Hex (число в шестнадцатеричной системе счисления).
# Реализуй в классах следующие методы:
#     • __init__(number) — получает одно целое число number в десятичной системе счисления;
#     • __str__() — возвращает строку в формате «{Название класса}: {число в соответствующей системе счисления}»,
#     например «Hex: 7C».
#     • to_dec() — возвращает представление данного числа в десятичной системе счисления.
#     • операции сложения, вычитания, умножения, целочисленного деления чисел в соответствующей системе счисления
#     которые будут возвращать новый объект — экземпляр этого класса.
#
# При создании классов избегай лишнего дублирования кода, используй наследование и полиморфизм,
# используй класс Number (число) — базовый класс для следующих классов Bin, Oct, Hex.
#
# Считай с клавиатуры 3 строки. На первой и второй строке указаны целые числа (первое число всегда больше второго),
# на третьей строке указано название класса: Bin, Oct или Hex. Создай 2 экземпляра данного класса с параметрами,
# указанными на первой и второй строке. Выведи результаты операций сложения, вычитания, умножения,
# деления этих объектов на разных строках.
#
# Входные данные:
# Три строки — два целых числа и название класса.
# Выходные данные:
# Выводится 4 строки.
#
# Пример работы программы:
# h = Hex(167)
# print(h)
# print(to_dec(h))
# b1 = Bin(7)
# b2 = Bin(15)
# b3 = b1 + b2
# print(b3)
# print(to_dec(b3))
#
# Вывод:
# А7
# 167
# 10110
# 22
#
# Пример ввода:
# 65
# 59
# Hex
# Пример вывода:
# Hex: 7C
# Hex: 6
# Hex: EFB
# Hex: 1

class Number:
    ALPHABET = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def __init__(self, number, base):
        result = ''
        while number != 0:
            digit = number % base
            if digit >= 10:
                digit = self.ALPHABET[digit]
            result += str(digit)
            number //= base
        self.value = result[::-1]

    def __str__(self):
        return f'{self.__class__.__name__}: {self.value}'

    def __add__(self, other):
        return self.__class__(self.to_dec() + other.to_dec())

    def __sub__(self, other):
        return self.__class__(self.to_dec() - other.to_dec())

    def __mul__(self, other):
        return self.__class__(self.to_dec() * other.to_dec())

    def __floordiv__(self, other):
        return self.__class__(self.to_dec() // other.to_dec())


class Bin(Number):
    def __init__(self, number):
        super().__init__(number, 2)

    def to_dec(self):
        return int(self.value, 2)


class Oct(Number):
    def __init__(self, number):
        super().__init__(number, 8)

    def to_dec(self):
        return int(self.value, 8)


class Hex(Number):
    def __init__(self, number):
        super().__init__(number, 16)

    def to_dec(self):
        return int(self.value, 16)


n1 = int(input())
n2 = int(input())
s = input()
if s == 'Bin':
    n1 = Bin(n1)
    n2 = Bin(n2)
elif s == 'Oct':
    n1 = Oct(n1)
    n2 = Oct(n2)
elif s == 'Hex':
    n1 = Hex(n1)
    n2 = Hex(n2)

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 // n2)

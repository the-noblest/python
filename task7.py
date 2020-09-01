from random import randint

import enum


class Matrix:
    __slots__ = ('matrix',)

    def __init__(self, matrix: list = None):
        self.matrix = matrix if matrix else [[randint(-10, 10) for _ in range(3)] for _ in range(3)]

    def __str__(self):
        return '\n'.join(list(map(str, self.matrix)))

    def __add__(self, other: "Matrix"):
        result = list()
        for sublist in zip(self.matrix, other.matrix):
            result.append(list(map(sum, zip(sublist[0], sublist[1]))))
        return Matrix(result)


class Clothes(enum.Enum):
    suit = 'для костюма'
    coat = 'для пальто'


class Tissue:
    __slots__ = ('__clothes', 'measure')

    def __init__(self, clothes, measure):
        if clothes not in Clothes:
            raise ValueError('Недопустимый вид одежды')
        self.__clothes = clothes

        if measure <= 0:
            raise ValueError('Недопустимый размер одежды')
        self.measure = measure

    @property
    def suit(self):
        return 2 * self.measure + 0.3

    @property
    def coat(self):
        return round(self.measure / 6.5 + 0.5, 2)

    def __str__(self):
        return f'{getattr(self, self.__clothes.name)} куб. м {self.__clothes.value}'


class Cell:
    __slots__ = ('__number',)

    def __init__(self, number):
        self.__number = number

    def __str__(self):
        return str(self.__number)

    def __add__(self, other: "Cell"):
        return Cell(self.__number + other.__number)

    def __sub__(self, other: "Cell"):
        result = self.__number - other.__number
        if result < 0:
            raise ValueError('Отрицательные числа недопустимы')
        return Cell(result)

    def __mul__(self, other: "Cell"):
        return Cell(self.__number * other.__number)

    def __truediv__(self, other: "Cell"):
        try:
            result = self.__number / other.__number
        except ZeroDivisionError:
            print('Деление на нуль недопустимо')
            return None
        return Cell(int(result))

    def make_orders(self, number_in_row):
        __temp = self.__number
        result_str = ''
        while __temp > number_in_row:
            result_str += '*' * number_in_row + '\n'
            __temp -= number_in_row
        result_str += '*' * __temp
        return result_str


def main():
    print('1-я задача:')
    first_matrix = Matrix()
    print(f'1-я матрица:\n{first_matrix}')
    second_matrix = Matrix()
    print(f'2-я матрица:\n{second_matrix}')
    print(f'Сумма:\n{first_matrix + second_matrix}')

    print('----------------------------------------------------')
    print('2-я задача:')
    volume = Tissue(Clothes.coat, 5)
    print(volume)
    volume = Tissue(Clothes.suit, 3)
    print(volume)

    print('----------------------------------------------------')
    print('3-я задача:')
    first_cell = Cell(8)
    second_cell = Cell(4)
    first_cell += second_cell
    print(first_cell.make_orders(5))


if __name__ == '__main__':
    main()

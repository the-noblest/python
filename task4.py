from functools import reduce
from math import factorial


# первый элемент не может подходить по определению
def second_task(input_list):
    print('----------------------------------------------------')
    print('2-я задача:')
    return [number for idx, number in enumerate(input_list[1:]) if number > input_list[idx]]


def third_task():
    print('----------------------------------------------------')
    print('3-я задача:')
    return [number for number in range(20, 241) if number % 20 == 0 or number % 21 == 0]


def forth_task(input_list):
    print('----------------------------------------------------')
    print('4-я задача:')
    return [number for idx, number in enumerate(input_list) if number not in input_list[:idx] + input_list[idx+1:]]


def fifth_task():
    print('----------------------------------------------------')
    print('5-я задача:')
    return reduce(lambda x, y: x*y, [number for number in range(100, 1001) if not number & 1])


def fact(number):
    for num in range(1, number + 1):
        yield factorial(num)


def seven_task(number):
    print('----------------------------------------------------')
    print('7-я задача:')
    for el in fact(number):
        print(el)


def main():
    print(second_task([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]))
    print(third_task())
    print(forth_task([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))
    print(fifth_task())
    seven_task(5)


if __name__ == '__main__':
    main()

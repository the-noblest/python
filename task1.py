from time import gmtime, strftime


def first_task():
    print('1-я задача:')
    first_var = input('Введите первую переменную:')
    second_var = input('Введите вторую переменную:')
    print(f'Вы ввели: {first_var} и {second_var}')


def second_task():
    print('----------------------------------------------------')
    print('2-я задача:')
    while True:
        try:
            seconds_number = int(input('Введите кол-во секунд:'))
            break

        except TypeError:
            print('Некорректный ввод')

    return strftime("%H:%M:%S", gmtime(seconds_number))


def number_check():
    while True:
        number = input('Введите число:')
        try:
            int(number)
            break

        except TypeError:
            print('Некорректный ввод')

    return number


def third_task():
    print('----------------------------------------------------')
    print('3-я задача:')
    number = number_check()

    return int(number) + int(number * 2) + int(number * 3)


# с while не так красиво, конечно
def forth_task():
    print('----------------------------------------------------')
    print('4-я задача:')
    number = number_check()

    largest_digit = 0
    num = 0

    while num < len(number):
        current_digit = int(number[num])

        if current_digit > largest_digit:
            largest_digit = current_digit

        num += 1

    return f'Наибольшая цифра: {largest_digit}'


def fifth_task():
    print('----------------------------------------------------')
    print('5-я задача:')
    revenues = int(input('Введите объем выручки:'))
    costs = int(input('Введите объем издержек:'))

    if revenues < costs:
        print('Убытки')

    else:
        income = revenues - costs
        print(f'Прибыль, рентабельность: {round(income / revenues, 2)}')

        staff = int(input('Введите кол-во сотрудников:'))
        print(f'Прибыль: {round(income / staff, 2)}')


def sixth_task():
    print('----------------------------------------------------')
    print('6-я задача:')
    while True:
        a = int(input('Введите кол-во километров:'))
        b = int(input('Введите кол-во километров для цели:'))

        if a > b:
            print('Некорректный ввод')
        else:
            break

    days_number = 1
    while a < b:
        a *= 1.1
        days_number += 1

    return f'Для достижения цели потребуется {days_number} дней'


def main():
    first_task()
    print(second_task())
    print(third_task())
    print(forth_task())
    fifth_task()
    print(sixth_task())


if __name__ == '__main__':
    main()

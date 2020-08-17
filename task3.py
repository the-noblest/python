from functools import reduce


def first_task(x, y):
    print('----------------------------------------------------')
    print('1-я задача:')
    try:
        return f'Результат: {x / y}'
    except ZeroDivisionError:
        return 'Деление на 0 за пределами матанализа запрещено!'


def second_task(name, surname, birth_year, location, email, phone):
    print('----------------------------------------------------')
    print('2-я задача:')
    return {
        'name': name, 'surname': surname, 'birth_year': birth_year, 'location': location, 'email': email, 'phone': phone
    }


def third_task(x, y, z):
    print('----------------------------------------------------')
    print('3-я задача:')
    return f'Результат: {max(x + y, x + z, y + z)}'


def pow_first_way(x, y):
    return f'Первый способ: {x ** y}'


def pow_second_way(x, y):
    num = 1
    for i in range(y):
        num *= x
    return f'Второй способ: {num}'


def forth_task(x, y):
    print('----------------------------------------------------')
    print('4-я задача:')
    return pow_first_way(x, y), pow_second_way(x, y)


def fifth_task():
    print('----------------------------------------------------')
    print('5-я задача:')

    numbers_list = list()
    total_sum = 0
    quit_flag = False

    while True:
        current_numbers_list = [num for num in input('Введите числа через пробел: ').split()]
        if current_numbers_list == ['q']:
            print('Выход...')
            break

        elif 'q' in current_numbers_list:
            del current_numbers_list[current_numbers_list.index('q')]
            quit_flag = True

        current_numbers_list = list(map(int, current_numbers_list))
        numbers_list += current_numbers_list

        current_sum = reduce(lambda x, y: x + y, current_numbers_list)
        total_sum += current_sum
        print(f'Сумма ряда чисел: {total_sum}')

        if quit_flag:
            print('Выход...')
            break


def int_func(word):
    return word.capitalize()


def sixth_task():
    print('----------------------------------------------------')
    print('6-я задача:')
    words_list = [word for word in input('Введите слова через пробел: ').split()]
    return list(map(lambda x: int_func(x), words_list))


def main():
    print(first_task(3, 5))
    print(second_task('Гадя', 'Хренова', 1861, 'Сызрань', 'g.khrenova@mail.ru', 88005553535))
    print(third_task(3, 4, 5))
    print(forth_task(2, 0))
    fifth_task()
    print(sixth_task())


if __name__ == '__main__':
    main()

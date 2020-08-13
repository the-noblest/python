def first_task():
    print('----------------------------------------------------')
    print('1-я задача:')
    types_list = [1, 2.0, 'three', [4, '5'], (6, 'seven'), {'8': 9.0}]
    for item in types_list:
        print(f'{item} type is {type(item)}')


def second_task():
    print('----------------------------------------------------')
    print('2-я задача:')
    numbers_list = [int(x) for x in input('Введите числа через пробел: ').split()]
    for i in range(0, len(numbers_list) - 1, 2):
        numbers_list[i], numbers_list[i+1] = numbers_list[i+1], numbers_list[i]
    return numbers_list


def search_month_by_dict(number):
    months_dict = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
    for season, months_range in months_dict.items():
        if number in months_range:
            return season


def search_month_by_list(number):
    months_list = [('winter', [12, 1, 2]), ('spring', [3, 4, 5]), ('summer', [6, 7, 8]), ('autumn', [9, 10, 11])]
    for season in months_list:
        if number in season[1]:
            return season[0]


def third_task():
    print('----------------------------------------------------')
    print('3-я задача:')
    while True:
        try:
            number = int(input('Введите номер месяца: '))
            if number in range(1, 13):
                break
            else:
                print('Попробуйте еще раз')
        except ValueError:
            print('Попробуйте еще раз')
    return f'{search_month_by_dict(number)}, {search_month_by_list(number)}'


def forth_task():
    print('----------------------------------------------------')
    print('4-я задача:')
    words_list = [x for x in input('Введите слова через пробел: ').split()]
    for num, word in enumerate(words_list):
        if len(word) > 10:
            print(f'{num}. {word[:10]}')
        else:
            print(f'{num}. {word}')


def fifth_task():
    print('----------------------------------------------------')
    print('5-я задача:')
    rate_list = [7, 5, 3, 3, 2]
    print(f'Текущий список: {rate_list}')
    while True:
        try:
            number = int(input('Введите число (или символы для выхода): '))
        except ValueError:
            break
        rate_list.append(number)
        rate_list = sorted(rate_list, reverse=True)
        print(f'Текущий список: {rate_list}')


def add_good_info():
    name = input('Введите название товара: ')
    while True:
        try:
            price = int(input('Введите цену товара: '))
            break
        except ValueError:
            print('Попробуйте еще раз')
    while True:
        try:
            count = int(input('Введите кол-во товара: '))
            break
        except ValueError:
            print('Попробуйте еще раз')
    measure = input('Введите единицу измерения: ')
    return {'название': name, 'цена': price, 'кол-во': count, 'ед.': measure}


def goods_analytics(goods_list):
    goods_stat = {'название': [], 'цена': [], 'кол-во': [], 'ед.': []}
    for good in goods_list:
        for parameter in goods_stat:
            value = good[1][parameter]
            if value not in goods_stat[parameter]:
                goods_stat[parameter].append(value)
    return goods_stat


def sixth_task():
    print('----------------------------------------------------')
    print('6-я задача:')
    goods_list = list()
    num = 1
    while True:
        goods_list.append((num, add_good_info()))
        num += 1
        if input('Добавить еще товар? (д/н) ') != 'д':
            break
    print(goods_list)
    print(goods_analytics(goods_list))


def main():
    first_task()
    print(second_task())
    print(third_task())
    forth_task()
    fifth_task()
    sixth_task()


if __name__ == '__main__':
    main()

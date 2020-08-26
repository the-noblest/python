from json import dump
from os import path
from statistics import mean


FIRST_FILE = path.join('text', 'test1.txt')
SECOND_FILE = path.join('text', 'test2.txt')
THIRD_FILE = path.join('text', 'test3.txt')
FORTH_FILE = path.join('text', 'test4.txt')
FORTH_NEW_FILE = path.join('text', 'test4_new.txt')
FIFTH_FILE = path.join('text', 'test5.txt')
SIXTH_FILE = path.join('text', 'test6.txt')
SEVENTH_FILE = path.join('text', 'test7.txt')
SEVENTH_JSON_FILE = path.join('text', 'test7.json')


def first_task():
    try:
        with open(FIRST_FILE, 'w', encoding='utf-8') as f:
            while True:
                string = input('Введите строку: ')
                if string == '':
                    break
                f.write(string + '\n')

    except FileNotFoundError:
        return None


def second_task():
    try:
        with open(SECOND_FILE, 'r', encoding='utf-8') as f:
            lines_count = 0
            words_count = 0

            for line in f:
                lines_count += 1
                words_count += len(line.split(' '))

            print(f'{lines_count} строк, {words_count} слов')

    except FileNotFoundError:
        return None


def third_task():
    try:
        with open(THIRD_FILE, 'r', encoding='utf-8') as f:
            sad_staff = list()

            for line in f:
                name, salary = line.split()
                if int(salary) < 20000:
                    sad_staff.append(name)

        return sad_staff

    except FileNotFoundError:
        return None

    except ValueError:
        return None


def forth_task():
    switch_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

    try:
        with open(FORTH_FILE, 'r', encoding='utf-8') as f_in:
            file_content = list()

            for line in f_in:

                for eng_word, rus_word in switch_dict.items():
                    if eng_word in line:
                        line = line.replace(eng_word, rus_word)

                file_content.append(line)

        with open(FORTH_NEW_FILE, 'w', encoding='utf-8') as f_out:
            f_out.writelines(file_content)

    except FileNotFoundError:
        return None


def fifth_task():
    try:
        input_list = [1, 4, 9, 7, 6]

        with open(FIFTH_FILE, 'w') as f_out:
            f_out.write(' '.join(list(map(str, input_list))))

        with open(FIFTH_FILE, 'r') as f_in:
            return sum(list(map(int, f_in.readline().split())))

    except FileNotFoundError:
        return None


def sixth_task():
    try:
        with open(SIXTH_FILE, 'r', encoding='utf-8') as f:
            subjects = dict()

            for line in f:
                subject = line.split()
                name = subject[0].rstrip(':')
                subjects[name] = 0

                for lessons in subject[1:]:
                    try:
                        subjects[name] += int(lessons[:len(lessons) - len(lessons.lstrip('0123456789'))])
                    except ValueError:
                        pass

        return subjects

    except FileNotFoundError:
        return None


def seventh_task():
    try:
        with open(SEVENTH_FILE, 'r', encoding='utf-8') as f_in:
            firms = dict()

            for line in f_in:
                firm = line.split()
                firms[firm[0]] = int(firm[2]) - int(firm[3])

        with open(SEVENTH_JSON_FILE, 'w') as f_out:
            dump([firms, {'average_profit': mean(firms.values())}], f_out)

    except FileNotFoundError:
        return None

    except ValueError:
        return None


def main():
    first_task()
    second_task()
    print(third_task())
    forth_task()
    print(fifth_task())
    print(sixth_task())
    seventh_task()


if __name__ == '__main__':
    main()

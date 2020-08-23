from itertools import count
from sys import argv


def main():
    try:
        number = int(argv[1])
    except ValueError:
        return None
    except IndexError:
        return None

    for el in count(number):
        if el > number + 10:
            break
        else:
            print(el)


if __name__ == '__main__':
    main()

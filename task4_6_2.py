from itertools import cycle
from sys import argv


def main():
    count = 0
    try:
        for el in cycle(argv[1]):
            if count > 10:
                break
            print(el)
            count += 1

    except IndexError:
        return None


if __name__ == '__main__':
    main()

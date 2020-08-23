from sys import argv


def main():
    try:
        work_hours = int(argv[1])
        norm = int(argv[2])
        bonus = int(argv[3])

        print(work_hours * norm + bonus)

    except ValueError:
        return None

    except IndexError:
        return None


if __name__ == '__main__':
    main()

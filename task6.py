from itertools import cycle
from time import sleep


def get_schedule():
    """
    Returns traffic light schedule in dict format.

    """
    traffic_light_dict = {'red': 7, 'yellow': 2, 'green': 5}
    schedule = [[color] * secs for color, secs in traffic_light_dict.items()]

    traffic_light_schedule = list()
    for color_time in schedule:
        traffic_light_schedule += color_time

    return traffic_light_schedule


class TrafficLight:
    __color = ''

    def running(self):
        """
        Generates traffic light work secondly according to schedule.

        """
        traffic_light_schedule = get_schedule()

        count = 0
        for color in cycle(traffic_light_schedule):
            if count > 30:
                break
            self.__color = color
            print(self.__color)
            count += 1
            sleep(1)


class Road:

    def __init__(self, length, width):
        self._length = length   # measure in metres
        self._width = width     # measure in metres

    def asphalt_weight(self, specific_weight, thickness):
        """
        Calculates asphalt weight for road covering (measure in tonnes).

        Arguments:
        specific_weight -- mass of asphalt for covering one square meter of the road with asphalt, 1 cm thick
        thickness -- thickness of asphalt (measure in cm)

        """
        return self._length * self._width * specific_weight * thickness / 1000


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False
    __status = 'Stopped'

    def go(self):
        self.speed += 30
        self.__status = 'Driving'
        print(self.__status)

    def stop(self):
        self.speed = 0
        self.__status = 'Stopped'
        print(self.__status)

    def turn(self, direction):
        self.__status = f'Turned to {direction}'
        print(self.__status)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    color = 'Grey'
    name = 'Toyota'

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed}: Over speed!')
        else:
            print(self.speed)


class WorkCar(Car):
    color = 'Yellow'
    name = 'Honda'

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed}: Over speed!')
        else:
            print(self.speed)


class SportCar(Car):
    color = 'Red'
    name = 'BMW'


class PoliceCar(Car):
    color = 'White'
    name = 'Ford'
    is_police = True


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисоки для {self.title}')


class Pen(Stationery):

    def draw(self):
        print(f'Pen: Запуск отрисоки для {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Pencil: Запуск отрисоки для {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Handle: Запуск отрисоки для {self.title}')


def main():
    print('----------------------------------------------------')
    print('1-я задача:')
    traffic_light = TrafficLight()
    traffic_light.running()

    print('----------------------------------------------------')
    print('2-я задача:')
    road = Road(5000, 20)
    print(road.asphalt_weight(25, 5))

    print('----------------------------------------------------')
    print('3-я задача:')
    first_employee = Position('Афанасий', 'Фет', 'Бухгалтер', 30000, 15000)
    print(first_employee.get_fullname(), first_employee.get_total_income())

    second_employee = Position('Александр', 'Пушкин', 'Редактор', 60000, 10000)
    print(second_employee.get_fullname(), second_employee.get_total_income())

    print('----------------------------------------------------')
    print('4-я задача:')
    work_car = WorkCar()
    print(work_car.name)
    work_car.go()
    work_car.show_speed()
    work_car.turn('right')
    work_car.go()
    work_car.show_speed()
    work_car.stop()
    work_car.show_speed()

    print('----------------------------------------------------')
    print('5-я задача:')
    pen = Pen('ручки')
    pen.draw()

    pencil = Pencil('карандаша')
    pencil.draw()

    handle = Handle('маркера')
    handle.draw()


if __name__ == '__main__':
    main()

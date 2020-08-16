'''1. Создать класс TrafficLight (светофор)
и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.'''
from time import sleep

class TrafficLight:

    def __init__(self, color, time):
        self.__name = color
        self.__time = time

    def __str__(self):
        reset = '\033[m'
        if self.__name == 'red':
            ld = "\033[31m\033[1m\033[3m\033[4mСтой пока  "
        elif self.__name == 'yellow':
            ld = "\033[33m\033[1m\033[3m\033[4mПриготовься "
        else:
            ld = "\033[32m\033[1m\033[3m\033[4mМожно ехать пока "

        return f'{ld}{self.__name.capitalize()}{reset} - горит {self.__time} секунд'

    # def running(self):
    #     while self.__time != 0:
    #         print(self)
    #         sleep(1)
    #         self.__time -= 1
    #     print()

    def running(self):
        print(self)
        sleep(self.__time)
        print()


led1 = TrafficLight('red', 7)
led2 = TrafficLight('yellow', 5)
led3 = TrafficLight('green', 15)
led1.running()
led2.running()
led3.running()

'''2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного
полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т'''


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._weight = 25

    def calc(self, deep=1):
        self.deep = deep
        self.mass = self._length * self._width * deep * self._weight

    def __str__(self):
        return f'{self._weight}м * {self._length}м * {self._weight}кг * {self.deep}см = {int(self.mass / 1000)} т'


asf = Road(width=20, length=5000)
asf.calc(7)
print(asf)

'''3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).'''


class Worker:

    def __init__(self, name, lastname, position, wage=45000, bonus=3500):
        self.name = name
        self.surname = lastname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        # self.__inc = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника - \033[031m{self.name} {self.surname}\033[m')

    def get_total_income(self):
        print(f'Зарплата \033[031m{self.name} {self.surname}\033[m составляет - \033[031m'
              f'{self._income["wage"] + self._income["bonus"]}$\033[m в год')

    def __str__(self):
        return f'{self.name} {self.surname} - {self.position}'


alex = Position('Alex', 'Ivanov', 'helper')
nik = Position('Nick', 'Goldman', 'foreman', 12 * 7000, 4250)
# print(nik._Worker__inc)
# print(alex._income)
alex.get_full_name()
nik.get_total_income()
print(alex, nik, sep='\n')

'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''


class Car:
    def __init__(self, speed=25, color='white', name='toyota', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def __str__(self):
        return self.name.capitalize()

    def show_speed(self):
        print(f'{self} have {self.speed} m/hour speed')

    def go(self):
        print(f'{self} go ahead!!!')

    def stop(self):
        print(f'{self} take a stop break')

    def turn(self, direction):
        print(f'{self} turn {direction}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'\033[031mAlarm: {self.speed} - m/hour!!!{TownCar.__name__.lower()} {self} - you ride very fast!'
                  f'\n   You should reduce speed\033[m')
            self.speed -= 20
        else:
            print(
                f'{TownCar.__name__.lower()} {self} - your speed is {self.speed}. Please drive carefully and have a good day!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'\033[031mAlarm: {self.speed} - m/hour!!!{WorkCar.__name__.lower()} {self} - you ride very fast!'
                  f'\n   You should reduce speed\033[m')
            self.speed -= 10
        else:
            print(
                f'{WorkCar.__name__.lower()} {self} - your speed is {self.speed}. Please drive carefully and have a good day!')


class PoliceCar(Car):
    pass


van = Car(25, 'black', 'sienna')
van.go()
van.stop()
van.turn('left')
van.show_speed()

tow = TownCar(75, 'blue', 'ford')
tow.go()
tow.show_speed()
tow.stop()
tow.go()
tow.show_speed()
tow.turn('right')

work = WorkCar(50)
work.go()
work.show_speed()
work.stop()
work.turn('u-turn')

police = PoliceCar(name='dodge', is_police=True)
police.go()
police.show_speed()
police.turn('back')
police.stop()

sport = SportCar(name='ferrari', speed=140, color='red')
sport.go()
sport.turn('left')
sport.show_speed()
sport.stop()

'''5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить
уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''


class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print(f'{self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}')



pero = Pen('Draw with pen')
crayon = Pencil('Draw with pencil')
brush = Handle('Draw with handle')
crayon.draw()
pero.draw()
brush.draw()


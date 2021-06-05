#задание_1
import time

class TrafficLight():
    __color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        for x in TrafficLight.__color:
            print(x)  
            if x == 'красный':
                time.sleep(7)
            elif x == 'жёлтый':
                time.sleep(2) 
            else:
                time.sleep(2) 

light = TrafficLight()
light.running()

#задание_2

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass_asf(self):
        return f'{self._length} m *{self._width} m * 15 kg * 0.08 m = {(self._length * self._width * 15 * 0.08) / 1000} t'

calc1 = Road(200, 180)
print(calc1.calc_mass_asf())

#задание_3
class Worker:

    def __init__ (self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position (Worker):
    def get_full_name (self):
        return f'{self.name} {self.surname}'

    def get_total_income (self):
        return f'{sum(self._income.values())}'

director = Position('John', 'Smith', 'director', 200000, 100000)
print(director.position)
print(director.get_full_name())
print(director.get_total_income())

#задание_4
class Car:
    def __init__ (self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        if direction == 0:
            print(f'{self.name} повернула направо')
        else:
            print(f'{self.name} повернула налево')

    def show_speed(self):
        print(f'{self.speed} - текущая скорость машины')
    
class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed} - вы превышаете разрешенную скорость')

class SportCar(Car):
    def show_speed(self):
        if self.speed > 90:
            print(f'{self.speed} - вы превышаете разрешенную скорость')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed} - вы превышаете разрешенную скорость')
    
class PoliceCar(Car):
    def __init__ (self, speed, color, name, is_police=True):
        Car.__init__ (self, speed, color, name, is_police)


audi = Car(80, 'black', 'audi')
toyota = TownCar(70, 'red', 'toyota')
reno = PoliceCar(60, 'white', 'reno')
ferrari = SportCar(120, 'yellow', 'ferrari')
ferrari.show_speed()
print(reno.is_police)
print(audi.color)
audi.go()
audi.stop()
toyota.show_speed()
toyota.turn(1)
reno.go()

#задание_5
class Stationery:

    def __init__ (self, title):
        self.title = title

    def draw (self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw (self):
        print(f'Для рисунка используется {self.title}.')


class Pencil(Stationery):
    def draw (self):
        print(f'Зарисовки, берём {self.title}.')

class Handle(Stationery):
    def draw (self):
        print(f'Рисует {self.title}.')

chalk = Stationery('chalk')
red_pen = Pen('красная ручка')
blue_pencil = Pencil('голубой карандаш')
yellow_handle = Handle('жёлтый маркер')

chalk.draw()
red_pen.draw()
blue_pencil.draw()
yellow_handle.draw()

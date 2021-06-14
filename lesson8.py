#задание_1
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        new_date = []

        for i in day_month_year.split():
            if i != '-': new_date.append(i)

        return int(new_date[0]), int(new_date[1]), int(new_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


my_day = Data('28 - 4 - 2021')
print(my_day)
print(Data.valid(18, 10, 2028))
print(my_day.valid(7, 13, 2000))
print(Data.extract('28 - 4 - 2021'))
print(my_day.extract('14 - 6 - 2021'))
print(Data.valid(4, 8, 2019))



#задание_2
class ZeroError(ZeroDivisionError):

    def __init__(self, variable):
        self.variable = variable

    def __truediv__(self, other):
        return self.variable // other.variable


inp_var1 = input('Введите число 1: ')
inp_var2 = input('Введите число 2: ')
    
try:
    inp_var1 = int(inp_var1)
    inp_var2 = int(inp_var2)
    if  inp_var2 == 0:
        raise ZeroError("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except ZeroError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_var1.__truediv__(inp_var2)}")


#задание_3
real_list = []
class TypeList(TypeError):

    def __init__(self, variable):
        self.variable = variable


    def my_list():
        while True:
            i = input('Write the variable: ')
            if not i:
                break                  
            try:
                if i.isdigit() == False:
                    raise TypeError("Вы ввели не число")
            except TypeError as err:
                print(err)
            else:
                real_list.append(i)
                print(f"Все хорошо. Ваш список: {real_list}")

TypeList.my_list()

#задание_4,5,6
big_store = {}
dep_store = {}
class Store:
    
    def __init__(self, name_of_row, department, name, quantity):
        self.name_of_row = name_of_row
        self.department = department
        self.name = name
        self.quantity = quantity

    def reception(name, quantity):
        if big_store.setdefault(name):
            big_store[name] += quantity
        else:
            big_store[name] = quantity        

        print(big_store)
        try:
            if quantity == str:
                raise TypeError("Вы ввели не число")
        except TypeError as err:
            print(err)

    def transfer(department, name, quantity):
        if big_store.setdefault(name):
            big_store[name] -= quantity
            dep_store = {department: {name: quantity}}
        else:
            dep_store[name] = quantity
        print(dep_store)
        print(big_store)

        

class Technics:

    def __init__(self, name, quantity, org_type):
        self.name = name
        self.quantity = quantity
        self.org_type = org.type


class Printer(Technics):

    def __init__(self, color):
        self.color = color

class Scaner(Technics):

    def __init__(self, grade):
        self.grade = grade

class Xerox(Technics):

    def __init__(self, speed):
        self.speed = speed




Store.reception('printer', 20)
Store.reception('xerox', 30)
Store.transfer('managers', 'printer', 10)


#задание_7

class ComplexNumber:
    def __init__(self, e, b, *args):
        self.e = e
        self.b = b
        self.y = 'e + b * i'

    def __add__(self, other):
        print(f'Сумма y1 и y2 равна')
        return f'y = {self.e + other.e} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение y1 и y2 равно')
        return f'y = {self.e * other.e - (self.b * other.b)} + {self.b * other.e} * i'

    def __str__(self):
        return f'y = {self.e} + {self.b} * i'


y_1 = ComplexNumber(2, -4)
y_2 = ComplexNumber(1, 3)
print(y_1)
print(y_1 + y_2)
print(y_1 * y_2)

#задание1
name = 'Helen'
print (name)

age = 33
print(age)

salary = 25000.38
print(salary)

your_name = input('Как вас зовут?  ')
print(your_name)

your_age = int(input('Сколько вам лет?  '))
print(your_age)

a = True
b = False
print(a,b)

#задание2
time = int(input('Введите время в секундах: '))
print(time)
time1 = time // 3600
time2 = time//60 - time1*60
time3 = time - time1*3600 - time2*60
print(f' {time1}:{time2}:{time3} ')


#задание3
num = str(input('Введите число от 1: '))
num1 = num * 2
num2 = num * 3
num3 = int(num) + int(num1) + int(num2)
print(num3)


#задание4
num = input('Введите положительное число: ')

cycle = 0
max_value = int(num[-1])
value = int(num[0])
num_len = len(num)

if int(num) // 10 > 1:
    while cycle < len(num):
        if max_value < value:
            max_value = value
        if len(num) > 1:
            num = num[:-1]
        value = int(num[-1])
        cycle += 1
    print(max_value)
else:
    print(num  - 'это самое большое число')

#задание5
billing = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))

if billing > costs:
    print('Вы получили прибыль!')
    profit = billing - costs
    rent = profit / billing
    workers = int(input('Введите количество работников: '))
    profit1 = profit / workers
    print('Рентабельность = ' + str(rent) +  ' Прибыль на одного сотрудника = ' + str(profit1))
else:
    print('Вы вышли в убыток!')


#задание6
a = int(input('Введите стартовое значение '))
b = int(input('Введите итоговое значение '))
c = 1
while a <= b:
    a = a + 0.1*a
    c += 1

print(c)

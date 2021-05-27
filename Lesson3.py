#задание_1
def my_f (var_1, var_2):
    var_3 = var_1 / var_2
    print(var_3)

var_1 = int(input("var_1: "))
var_2 = int(input("var_2: "))

if var_2 != 0:
    my_f(var_1, var_2)
else:
    print('На ноль делить нельзя!')

#задание_2
def peoples_list (name, surname, age_of_birth, city_of_living, email, number_of_phone):
    print(f"name - {name}; surname - {surname}; age_of_birth - {age_of_birth}; city_of_living - {city_of_living}; email - {email}; number_of_phone - {number_of_phone}")
    
peoples_list(name='Frank', surname='Smith', age_of_birth=42, city_of_living='Chicago', email= 'fr42@gmail.com', number_of_phone= 89994522544)

#задание_3
def max_sum (var_1, var_2, var_3):
    if var_1 < var_2 and var_1 < var_3:
        return var_2 + var_3
    elif var_2 < var_3 and var_2 < var_1:
        return var_1 + var_3
    else:
        return var_1 + var_2

print(max_sum(10, 12, 20))

#второй_вариант задание_3
def max_sum2(var_1, var_2, var_3):
    return (var_1 + var_2 + var_3) - min(var_1, var_2, var_3)

print(max_sum2(10, 14,25))

#задание_4
def my_func4 (x, y):
    if x > 0 and y < 0:
        return x**y
    else:
        print('Введите корректные значения!')

print(my_func4(2, -2))

#второй_вариант задание_4
def my_func5 (x, y):
    if x > 0 and y < 0:
        for i in range(abs(y)-1):
            x*=x
        return 1/x
    else:
        print('Введите корректные значения!')

print(my_func5(2, -2))

#задание_5
def my_sum ():
    run = True
    summm = 0
    while run:
        num_list = input(' ')
        num_list = num_list.split(sep=" ")
        if num_list[-1] == '*':
            num_list.pop(-1)
            num_list = [int(i) for i in num_list]  
            summm += sum(num_list)
            print(summm)
            break
        else:
            num_list = [int(i) for i in num_list]  
            summm += sum(num_list)
            print(summm)
    

my_sum()

#задание_6
def int_func():
    some_text = input('Введите слово строчными буквами: ')
    if some_text.islower():
        print(some_text.title())
    else:
        print('Вы ошиблись, введите слово еще раз!')


int_func()

#задание_7
def int_func():
    some_text = input('Введите предложение строчными буквами:  ')
    if some_text.islower():
        print(some_text.title())
    else:
        print('Вы ошиблись, введите еще раз!')


int_func()
#задание 1
My_list = [241, 'Hello', 2.587, True, (99, 25, 17), {'lucky number': 77}]
print(type(My_list[0]))
print(type(My_list[1]))
print(type(My_list[2]))
print(type(My_list[3]))
print(type(My_list[4]))
print(type(My_list[5]))

#задание 2
new_list2 = []
run = True
while run:
    new_values = input("Введите значение: ")
    if new_values == 'end' or new_values == 'esc':
        break
    new_list2.append(new_values)
print(new_list2)

step = 0
for i in range(int(len(new_list2)/2)):
    new_list2[step], new_list2[step+1] = new_list2[step+1], new_list2[step]
    step +=2
print(new_list2)

#задание 3
dict_of_month = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
new_value = int(input('Введите число от 1 до 12: '))
print(dict_of_month.get(new_value))

list_of_month = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
new_value1 = int(input('Введите число от 1 до 12: '))
print(list_of_month[new_value1-1])

#задание 4
some_text = input('print some long text: ')
some_list = some_text.split( )
for number, i in enumerate(some_list):
    print(str(number+1) + '. ' + i[0:10])

#задание 5
rating_list = [7, 7, 5, 3, 3, 2, 2, 1, 1]
while run:
    new_rating = input("print some new rating: ")
    if new_rating == 'end' or new_rating == 'esc':
        break
    rating_list.append(int(new_rating))
    rating_list.sort(reverse=True)
    print(rating_list)

#задание 6
product_list = []
iterator = 1
while run:
    new_dict = dict()
    new_dict ['название'] = input('Введите название товара: ')
    new_dict ['цена'] = input('Введите цену товара: ')
    new_dict ['количество'] = input('Введите количество товара: ')
    new_dict ['ед.'] = input('Введите единицу измерения товара: ')
    new_tuple = (iterator, new_dict)
    product_list.append(new_tuple)
    out_message = int(input('Если хотите продолжить, введите 1. Нет - 0: '))
    if out_message == 0:
        break
    iterator += 1

print(product_list)

analyst_dict = {}
temp_list_name = []
temp_list_price = []
temp_list_amount = []
temp_list_ed = []

for list_items in product_list:
    tuple_num, tuple_dict = list_items
    temp_list_name.append(tuple_dict.get('название'))
    temp_list_price.append(tuple_dict.get('цена'))
    temp_list_amount.append(tuple_dict.get('количество'))
    temp_list_ed.append(tuple_dict.get('ед.'))

analyst_dict['название'] = temp_list_name
analyst_dict['цена'] = temp_list_price
analyst_dict['количество'] = temp_list_amount
analyst_dict['ед.'] = temp_list_ed

print(analyst_dict)
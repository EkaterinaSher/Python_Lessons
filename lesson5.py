#задание_1
with open ('new_les5.2.txt', 'w') as a:
    while True:
        i = input('Write the sentense: ')
        if not i:
            break
        a.write(f'{i}\n')

    
#задание_2
with open ('doc1.txt', 'r') as a:
    line_count = 0
    for line in a:
        line_count += 1
        print(f'Количество слов в строке {line_count} - {len(line.split( ))}')
print(f'Количество строк - {line_count}')

#задание_3
with open ('doc2.txt', 'r', encoding='utf-8') as f:
    string = ''
    line_count = 0
    sm = 0
    for line in f:
        string = line.split( )
        if int(string[2]) < 20000:
            print(string[0])
        line_count += 1
        sm += int(string[2])
    print("Average Salary - " + str(sm/line_count))

#задание_4
with open ('doc3.txt', 'r', encoding='utf-8') as a:
    string1 = ''
    for line in a:
        string1 = line.split( )
        if string1[0] == 'One':
            string1[0] = 'Один'
        if string1[0] == 'Two':
            string1[0] = 'Два'
        if string1[0] == 'Three':
            string1[0] = 'Три'
        if string1[0] == 'Four':
            string1[0] = 'Четыре'
        with open ('doc4.txt', 'a', encoding='utf-8') as f:
            f.write(f'{string1}\n')

#задание_5
with open ('doc5.txt', 'w') as s:
    a = 4
    s.write(f'{a}\t')
    b = 8
    s.write(f'{b}\t')
    c = 15
    s.write(f'{c}\t')
    d = a + b + c
    s.write(f'Sum of numbers: {d}')

#задание_6
with open ('doc6.txt', 'r', encoding='utf-8') as m:
    my_dict = { }
    summm = 0
    import re
    for line in m:
        ints = re.findall("\d+", line)
        strr = re.findall("[А-я]+", line)
        ints = [int(i) for i in ints]  
        summm = sum(ints)
        my_dict[strr[0]] = summm
    print(my_dict)       

#задание_7
with open ('doc7.txt', 'r') as n:
    string = ''
    profit = 0
    line_count = 0
    sm = 0
    new_dict = {}
    new_dict2 = {}
    new_list = []
    for line in n:
        string = line.split( )
        print(string)
        profit = int(string[2]) - int(string[3])        
        print(profit)
        new_dict[string[0]] = profit
        if profit > 0:
            sm += int(profit)
            line_count += 1
    new_dict2['average_profit'] = sm/line_count
    new_list.append(new_dict)
    new_list.append(new_dict2)
    print(new_list)
    import json
    with open ('new.json', 'w') as v:
        data = json.dump(new_list, v)
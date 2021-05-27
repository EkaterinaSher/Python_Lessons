#задание_1
from sys import argv

def salary_emp (listo):
    return (int(listo[1])*int(listo[2]))+int(listo[3])
    

print(salary_emp(argv))

#задание_2
just_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = list(el1 for countero, el1 in enumerate(just_list) if el1 > just_list[countero - 1])
print(new_list[1:])


#задание_3
new_set = {el for el in range(20,241) if el % 20 == 0 or el % 21 == 0}
print(new_set)

#задание_4
from collections import OrderedDict
my_list = [1, 1, 4, 5, 7, 3, 5, 6, 4, 7, 9]
new_list = [el for el in OrderedDict.fromkeys(my_list)]
print(new_list)

#задание_5
big_list = [el for el in range(100, 1001) if el % 2 == 0]
print(big_list)

from functools import reduce
def big_sum(prev_el, el):
    return prev_el * el
print(reduce(big_sum, big_list))

#задание_6
from itertools import count, cycle 
for el in count(2):
    if el > 18:
        break
    else:
        print(el)


i = 0
for el in cycle("hello"):
    if i > 12:
        break
    print(el)
    i += 1

#задание_7
from math import factorial
def fact(n):
    yield [factorial(el) for el in range(1, n+1)]

for i in fact(5):
    print(i)
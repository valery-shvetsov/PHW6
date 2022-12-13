# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, а второй - 
# сам элемент, при условии, что они не совпадают.

import random

def random_list (length_list, down_border, up_border):
    '''
    Задаем список случайных целых чисел в диапазоне между down_border и up_border
    длиной length_list
    '''
    rand_list=[]
    for i in range(0,length_list):
        rand_list.append(random.randint(down_border,up_border))
    return rand_list

print()
number_list=random_list (200,0,100)
result_tuple_1=[]
result_tuple_2=[]
number_tuple=list(enumerate(number_list))
for index,value in number_tuple:
    if index!=value:
        result_tuple_1.append((index,value))
    else:
        result_tuple_2.append((index,value))    
print('Не совпадающие кортежи')
print(result_tuple_1)
print('Совпадающие кортежи')
print(result_tuple_2)

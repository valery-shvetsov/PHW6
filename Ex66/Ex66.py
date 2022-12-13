# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

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
result_tuple=[]
number_tuple=list(enumerate(number_list))
for index,value in number_tuple:
    if (index+value)%5==0:
        result_tuple.append((index,value))
print(result_tuple)

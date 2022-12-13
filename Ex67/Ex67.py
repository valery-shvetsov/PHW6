 #Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

import random

def Random_list (length_list, down_border, up_border):
    '''
    Задаем список случайных целых чисел в диапазоне между down_border и up_border
    длиной length_list
    '''
    rand_list=[]
    for i in range(0,length_list):
        rand_list.append(random.randint(down_border,up_border))
    return rand_list


print()
number=int(input('Введите количество элементов списка (целое число более 1): '))
source_list=[]
source_list=Random_list(number, 10, 100)
print('Исходный список')
print(source_list)
result_list=[source_list[i] for i in range(len(source_list)) if (source_list[i]//10+source_list[i]%10)%2==0]
print('Список-результат')
print(result_list)
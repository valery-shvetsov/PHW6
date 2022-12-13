# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.


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
resalt_list=[]
source_list=Random_list(number, -10, 10)
print('Исходный список')
print(source_list)
length_list=len(source_list)
resalt_list=[source_list[i]*source_list[length_list-i-1]for i in range(length_list//2+length_list%2)]
print('Список произведений пар')
print(resalt_list)

# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

print()
def input_int(input_string):
    '''
    Ввод числа с пояснением
    '''
    while True:
        try:
            num=int(input(input_string))
            return num
        except ValueError:
            print('Введено не число. Давайте попробуем еще раз')

num=input_int ('Введите число более 0 :')
result_list=[(-3)**i for i in range (0,num)]
print(result_list)

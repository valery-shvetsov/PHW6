# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
# qwe asd zxc qwe ertqwe
# йцу фыв ячс цук йцукен йцу

print()
source_str=input('Введите строку в которой будет проходить поиск :\n')
#source_str='йцу фыв ячс цук йцукен йцу'
search_str=input('Введите строку, которую надо найти два раза :\n')
#search_str='йцу'
source_list=source_str.split(' ')
cont=0
a=list(enumerate(source_list))
for i,value in a:
#    print (i,value)
    if search_str in value:
        cont+=1
        if cont==2:
            print (i)




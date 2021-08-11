#Написать функцию, которая имитировала бы range для латиского алфавита
#Генерируем список из букв латинского алфавита, вычисляем индексы букв start и stop, генерируем список с помощью  полученных индексов

import string

def letters_range(min,max,step=1):
    lettesr=list(string.ascii_lowercase)
    min_index=lettesr.index(min)
    max_index=lettesr.index(max)
    return [lettesr[i] for i in range(min_index,max_index,step)]



# print(letters_range('b', 'w', 2))
# print(letters_range('a', 'g'))
# print(letters_range('g', 'p'))
# print(letters_range('p', 'g', -2))
# print(letters_range('a','a'))



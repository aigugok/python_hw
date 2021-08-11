numbers=["0","1","2","3","4","5","6","7","8","9"]
#палиндромы не заканчиваются на 0, так как мы работаем с двоиными палиндромами, то наши падиндромы не могут начинаться с четного числа
#1 - генерация десятичных палиндромов ф-ей generate_decimal_palindroms, которая принимает длину палиндромов в знаках (нам надо 1млн, то есть 6 знаков)
#   генерируем массив в котором будут нечетные числа и до истечении половины длины палиндрома(до 3) для каждого элемента прибавляем цифру
#ПОлучили  список вида ['1', '3', '5', '7', '9', '10', ..19, ..,90,..99, 100, 101,..,199, ..991,...999]. Палиндромы из них можно получить взяв и отзеркалив элементы 1 - 11, 100 - 100001, 978- 978789
# и отзеркалив элементы, убрав серединный из отзеркалинного, 123-12321, 987- 98789
#эти числа проверяем на то, являются ли они двоичными палиндромами переведя десятичный в двоичный вид и отзеркалив двоичный вид строки

def is_binary_palindrom(number):
    if(f'{int(number):b}' == f'{int(number):b}'[::-1]):
        global sum
        sum+=int(number)

def f(var):
    for i in numbers:
        new_var = var + i
        list.append(new_var)


def generate_decimal_palindroms(palindrom_len):
    for i in range(1,len(numbers),2):
        list.append(numbers[i])
    k=1
    len_min =0
    len_max=len(list)
    while k<palindrom_len//2:
        for i in range(len_min,len_max):
            f(list[i])
        k+=1
        len_min=len_max
        len_max=len(list)

list=[]
generate_decimal_palindroms(6)
sum=0
for i in list:
    is_binary_palindrom(i + i[::-1])
    is_binary_palindrom(i + i[-2::-1])
print(sum)




















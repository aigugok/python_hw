#Функция читает ввод пол-ля: если на вх - cancel заканчивает работу, если нет пробует перевести строку в число. Для четных чисел выводит целочисленное деление числа на 2, для нечетных - число*3+1
#Для нечисловых строк - Не удалось преобразовать введенный текст в число.
def recursion_func():
    str=input()
    if (str=="cancel"):
        print("Bye!")
        return
    try:
        str=int(str)
    except ValueError:
        print("Не удалось преобразовать введенный текст в число.")
        return recursion_func()
    if (str%2==0):
        print(str//2)
    else:
        print(str*3+1)
    return recursion_func()



recursion_func()


#Пользователь вводит неотрицательные целые числа,разделенные через пробел. На выходе - наименьшее положительное число, не входящее в данный пользователем
# список чисел

#введенные числа, разделенные пробелом, приводим к int проверяем на неотрицательность и добавляем в список
lst=[int(i) for i in input().split() if not int(i)<0]
i=min(lst)
if i>1:
    print("1")
else:
    while i in lst:
        i+=1
    print(i)


#Печать элементов в виде списка с неповторяющимися элементами. Входные данные - input пользователя
#set не использовала, так как в примере порядок элементов сохраняется, поэтому dict from keys - есть порядок + гарантируется уникальность

#вариант1
#1-input().split(" ") - сделать список, разбив строку по пробелам
#2-dict.fromkeys(list) - сделать словарь из ключей для того, что убрать повторяющиеся эл-ты и сохранить порядок
#3 - печать
print(*(dict.fromkeys(input().split(" "))))

#вариант2
#print(" ".join((dict.fromkeys(input().split(" ")))))

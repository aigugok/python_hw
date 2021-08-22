#Надо написать функцию которая возвращает N-мерный массив с ширинами заданными в аргументе списком из N элементов:n_arr([2,2]) - [[“”,“”],[“”,“”]], n_arr([2,2,2]) - [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]
#A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original. - copy.copy() method
#A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original. - copy.deepcopy()
import copy

def n_arr(list):
    if not len(list):
        return "Put a non-empty array"
    new_lst = ["" for i in range(list[0])]
    list.pop(0)
    while len(list):
        new_lst=[copy.deepcopy(new_lst) for i in range(list[0])]
        list.pop(0)
    return new_lst



# a=n_arr([5,2,3])
# print(a)
# a[0][0][1]="001"
# a[2][1][4]="214"
# print(a)


#Написать функцию-генератор, которая объединяет два отсортированных итератора (все элементы из каждой коллекции, в упорядоченном виде) -
# list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]

import itertools
def imerge(a, b):
    return iter(sorted(itertools.chain(a, b)))



# print(list(imerge((x for x in range(3,8)),(x for x in range(2,10)))))
#
# a=imerge((x for x in range(3,8)),(x for x in range(2,10)))
# print(next(a))
# print(next(a))
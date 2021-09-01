#Написать функцию-генератор, которая объединяет два отсортированных итератора (все элементы из каждой коллекции, в упорядоченном виде) -
import itertools

def f(x,y):
    i=next(x)
    j=next(y)
    x_stop=0
    y_stop=0
    while True:
        if x_stop==1 and y_stop==1:
            return

        if i<j and x_stop==0:
            yield i
            try:
                i = next(x)
            except StopIteration:
                x_stop=1

        elif i> j and y_stop==0:
            yield j
            try:
                j = next(y)
            except StopIteration:
                y_stop=1

        else:
            if x_stop==0:
                yield i
            if y_stop == 0:
                yield j
            try:
                i = next(x)
            except StopIteration:
                x_stop=1
            try:
                j = next(y)
            except StopIteration:
                y_stop=1


if __name__ == '__main__':
    #a=f(itertools.count(8),itertools.count(3))
    #a=f((x for x in range(2,5)),(x for x in range(10,15)))
    a = f((x for x in range(10, 15)), (x for x in range(2, 5)))
    for i in range(20):
        print(next(a))
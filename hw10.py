#Пол-ль вводит натуральное число, на выходе получает посл-ть для расчета гипотезы Коллатца и кол-во шагов

def Collatz_hypothesis(n,step=0):
    print(n)
    if (n<1):
        print("это не натуральное число")
        return
    if n==1:
        print(f"Всего получаем {step} шагов.")
        return
    if(n%2==0):
        return Collatz_hypothesis(n//2,step+1)
    return Collatz_hypothesis(n*3+1,step+1)


try:
    num=int(input())
    Collatz_hypothesis(num)
except ValueError:
    print("Не удалось преобразовать введенный текст в число.")
